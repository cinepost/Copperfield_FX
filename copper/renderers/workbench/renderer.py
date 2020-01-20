import logging
import math
import time
import moderngl
from OpenGL.GL import *
from OpenGL.arrays.vbo import VBO

import moderngl
import ghalton
from PIL import Image

from time import sleep
from enum import IntEnum
from ctypes import c_float
import numpy as np
from pyrr import Matrix44

from PyQt5 import QtCore

from copper import hou
from copper.core.utils import Singleton
from copper.core.vmath import Matrix4, Vector3
from copper.ui.panels.scene_view_panel.camera import Camera

from copper.ui.context_manager import ContextManager

from .drawable import QuadFS
from .scene import Scene

logger = logging.getLogger(__name__)


class RenderPasses(IntEnum):
    BEAUTY = 0
    DIFFUSE = 1
    SPECULAR = 2
    NORMALS = 3
    OCCLUSION = 4

class SignalsIPR(QtCore.QObject):
    start = QtCore.pyqtSignal(int, int)
    update_sample = QtCore.pyqtSignal()

class WorkbenchIPR(QtCore.QObject):
    def __init__(self, scene=None, camera=Camera()):
        super().__init__()
        self.thread = QtCore.QThread()
        self.thread.setTerminationEnabled(True)
        self.thread.start()
        self.thread.setPriority(QtCore.QThread.TimeCriticalPriority)
        
        self.signals = SignalsIPR()

        self.renderer = Workbench(scene, camera)
        self.renderer.moveToThread(self.thread)
        self.signals.start.connect(self.renderer.runIPR)

        self.width, self.height = None, None

    def setImageUpdateHandler(self, handler):
        self.renderer.signals.sample_rendered.connect(handler)

    def updateCamera(self, camera):
        self.renderer._camera = camera
        self.reset()

    def start(self, width, height, samples = 16):
        if (self.width, self.height) != (width, height):
            self.width, self.height = width, height
            self.reset()
        elif not self.renderer.isRunningIPR():
            self.signals.start.emit(width, height)

    def stop(self):
        self.renderer._is_running_ipr = False
    
    def reset(self):
        self.renderer._is_running_ipr = False
        self.signals.start.emit(self.width, self.height)
        
    def terminate(self):
        self.thread.terminate()

    @property
    def image_data(self):
        return self.renderer._image_data

class Signals(QtCore.QObject):
    request_render_sample_pass = QtCore.pyqtSignal()
    sample_rendered = QtCore.pyqtSignal()
    start_progressive_render = QtCore.pyqtSignal()
    stop_progressive_render = QtCore.pyqtSignal()
    reset_progressive_render = QtCore.pyqtSignal()

class Workbench(QtCore.QObject):
    def __init__(self, scene=None, camera=Camera()):
        QtCore.QObject.__init__(self)
        self.ctx = None

        self._initialized = False
        self._is_running_ipr = False
        self._progressive_update = False

        self._frame_buffer = None # final composited frame
        self._render_buffer = None 

        self._width = None
        self._height = None

        self._camera = camera

        self._image_data = None

        # helpers
        self.m_identity = Matrix44.identity() # just a helper
        
        # signals
        self.signals = Signals()

        logger.debug("Workbench Renderer created")
    
    @property
    def scene(self):
        return self._scene

    def availableRenderPasses(self):
        return {
            "Beauty"    : RenderPasses.BEAUTY,
            "Diffuse"   : RenderPasses.DIFFUSE,
            "Specular"  : RenderPasses.SPECULAR,
            "Normals"   : RenderPasses.NORMALS,
            "Occlusion" : RenderPasses.OCCLUSION
        }

    def init(self, width, height, render_samples = 16):
        if not self._initialized:
            self.ctx = ContextManager.get_offscreen_context()
            
            self._scene = Scene(self.ctx)
            self._scene.init()
            
            # A fullscreen quad just for rendering one pass to offscreen textures
            self.quad_fs = QuadFS(self.ctx)
            self.quad_fs.m_model.write(Matrix44.identity().astype('f4').tobytes())
            self.quad_fs.m_view.write(Matrix44.identity().astype('f4').tobytes())
            self.quad_fs.m_proj.write(Matrix44.orthogonal_projection(-1, 1, 1, -1, 1, 10).astype('f4').tobytes())
            self.quad_fs.flip_v.value = 0

            # aa sampler
            self.setRenderSamples(render_samples)

            self._initialized = True
            print("Workbench initialized")

        if (self._width, self._height) != (width, height):
            self.resize(width, height)

    @QtCore.pyqtSlot(int, int)
    def runIPR(self, w, h): # run / rerun interactive renderer
        self._is_running_ipr = True
        self.render_sample_num = 0
        self.renderIPRPassSample = self.renderPassSample
        self.init(w, h)

        while self._is_running_ipr:
            self.renderIPRPassSample()

        self.renderIPRPassSample = self.nofunc

    def isRunningIPR(self):
        return self._is_running_ipr

    def nofunc(self):
        pass

    def setRenderSamples(self, samples):
        self.render_samples = samples
        self.render_sample_num = 0
        self.quad_fs.program['aa_passes'].value = self.render_samples

        sequencer = ghalton.GeneralizedHalton(ghalton.EA_PERMS[:2])
        self.sampling_points = sequencer.get(samples)

    def renderFrame(self) -> np.ndarray:
        self.render_sample_num = 0
        for i in range(self.render_samples):
            self.renderPassSample(intermediate_sample_update=False)

        return self._image_data


    def renderPassSample(self, intermediate_sample_update=True):
        #print("Workbench render image sample %s" % self.render_sample_num)
        m_view = self._camera.getTransform()
        m_proj = self._camera.getProjection(jittered=True, point=self.sampling_points[self.render_sample_num])

        # Render the scene to offscreen buffer
        self._render_buffer.use()
        self._render_buffer.clear(0.0, 0.0, 0.0, 0.0)

        self.ctx.multisample = False
        self.ctx.disable(moderngl.DEPTH_TEST)

        # Render the scene
        self._scene.background.draw()

        self.ctx.enable(moderngl.DEPTH_TEST)

        # geometry
        for drawable in self.scene.shapes():
            drawable.surface_prog["model"].write(self.m_identity.astype('f4').tobytes())
            drawable.surface_prog["view"].write(m_view.astype('f4').tobytes())
            drawable.surface_prog["projection"].write(m_proj.astype('f4').tobytes())
            drawable.draw()

        # clear if it's first pass
        if self.render_sample_num == 0:
            self._frame_buffer.clear(0.0, 0.0, 0.0, 0.0)

        # Render buffer to frame buffer
        # Activate the window screen as the render target
        self._frame_buffer.use()
        self._render_buffer_albedo.use(location=0)
        self.quad_fs.flip_v.value = 0
        self.quad_fs.program['aa_pass'].value = self.render_sample_num
        
        self.ctx.disable(moderngl.DEPTH_TEST)        
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_equation = moderngl.FUNC_ADD
        self.ctx.blend_func = moderngl.SRC_ALPHA, moderngl.ONE_MINUS_SRC_ALPHA
        self.quad_fs.flip_v.value = 1
        self.quad_fs.render()
        self.ctx.disable(moderngl.BLEND)
        
        self.ctx.finish()

        self.render_sample_num += 1

        if intermediate_sample_update or self.render_sample_num >= self.render_samples:
            self._frame_buffer.read_into(self._image_data, components=4, attachment=0, alignment=1, dtype='f2')       
            self.signals.sample_rendered.emit()

        if self.render_sample_num >= self.render_samples:
            self.render_sample_num = 0
            self._is_running_ipr = False

    def buildRenderBuffers(self, width, height):
        buffer_size = (width, height)

        # offscreen render target
        if self._render_buffer:
            self._render_buffer.release()
            self._render_buffer_albedo.release()
            self._render_buffer_metalness.release()
            self._render_buffer_roughness.release()
            self._render_buffer_normals.release()
            self._render_buffer_depth.release()

        self._render_buffer_albedo = self.ctx.texture(buffer_size, 4, dtype='f2') # RGBA color/diffuse layer
        self._render_buffer_metalness = self.ctx.texture(buffer_size, 1, dtype='f2') # RGBA color/diffuse layer
        self._render_buffer_roughness = self.ctx.texture(buffer_size, 1, dtype='f2') # RGBA color/diffuse layer
        self._render_buffer_normals = self.ctx.texture(buffer_size, 3, dtype='f2') # Textures for storing normals (16 bit floats)
        self._render_buffer_depth = self.ctx.depth_texture(buffer_size) # Texture for storing depth values

        # create a framebuffer we can render to
        self._render_buffer = self.ctx.framebuffer(
            color_attachments=[
                self._render_buffer_albedo,
                self._render_buffer_metalness,
                self._render_buffer_roughness,
                self._render_buffer_normals
            ],
            depth_attachment=self._render_buffer_depth,
        )
        self._render_buffer.viewport = (0, 0, width, height)

        if self._frame_buffer:
            self._frame_buffer.release()
            self._frame_buffer_diffuse.release()
            self._frame_buffer_depth.release()

        self._frame_buffer_diffuse = self.ctx.texture(buffer_size, 4, dtype='f2') # RGBA color/diffuse layer
        self._frame_buffer_depth = self.ctx.depth_texture(buffer_size) # Texture for storing depth values

        # create a framebuffer we can render to
        self._frame_buffer = self.ctx.framebuffer(
            color_attachments=[
                self._frame_buffer_diffuse,
            ],
            depth_attachment=self._frame_buffer_depth,
        )
        self._frame_buffer.viewport = (0, 0, width, height)

        # rendered data buffer
        self._image_data = np.empty((width, height), dtype="4float16")

    def resize(self, width, height):
        self._width, self._height = width, height
        self._camera.setViewportDimensions(width, height)
        
        self.ctx.viewport = (0, 0, width, height)
        self.buildRenderBuffers(width, height)