import math
import random
import numpy as np
from OpenGL.GL import *

from copper.core.vmath import Matrix4, Vector3
from pyrr import Matrix44

class Camera(object):
    def __init__(self, position=[5,5,5], target=[0,0,0], fov_degrees = 41.0, near_plane = 0.1, far_plane = 1000.0,
                    ortogrphic_width=50.0, is_perspective=True):
        self.is_perspective = is_perspective
        self.fov_degrees = self.default_fov_degrees = fov_degrees
        self.orbiting_speed_degrees_per_radians = 300.0

        self.near_plane = self.default_near_plane = near_plane
        self.far_plane = self.default_far_plane = far_plane

        # point of view, or center of camera; the ego-center; the eye-point
        self.position = self.default_position = Vector3(position)

        # point of interest; what the camera is looking at; the exo-center
        self.target = self.default_target = Vector3(target)

        # This is the up vector for the (local) camera space
        self.up = Vector3()

        # This is the up vector for the (global) world space;
        # it is perpendicular to the horizontal (x,z)-plane
        self.ground = Vector3([0,1,0])

        # During dollying (i.e. when the camera is translating into
        # the scene), if the camera gets too close to the target
        # point, we push the target point away.
        # The threshold distance at which such "pushing" of the
        # target point begins is this fraction of near_plane.
        # To prevent the target point from ever being clipped,
        # this fraction should be chosen to be greater than 1.0.
        self.target_push_threshold = 1.3

        # We give these some initial values just as a safeguard
        # against division by zero when computing their ratio.
        self.viewportWidthInPixels = 10
        self.viewportHeightInPixels = 10
        self.viewportRadiusInPixels = 5

        self.aspect_ratio = 1.0

        self.build_up()

    def reset(self):
        self.fov_degrees = self.default_fov_degrees
        self.near_plane = self.default_near_plane
        self.far_plane = self.default_far_plane
        self.position = self.default_position
        self.target = self.default_target
        self.build_up()

    def build_up(self):
        t2p = self.position - self.target
        left = -(t2p ^ self.ground).normalized()
        self.up = (t2p ^ left).normalized()

    def setViewportDimensions( self, widthInPixels, heightInPixels ):
        self.viewportWidthInPixels = widthInPixels
        self.viewportHeightInPixels = heightInPixels
        self.viewportRadiusInPixels = 0.5*widthInPixels if (widthInPixels < heightInPixels) else 0.5*heightInPixels

    def getProjection(self, jittered=False, point=None):
        tangent = math.tan( self.fov_degrees / 2.0 / 180.0 * math.pi )
        viewportRadius = self.near_plane * tangent
        if self.viewportWidthInPixels < self.viewportHeightInPixels:
            viewportWidth = 2.0 * viewportRadius
            viewportHeight = viewportWidth * self.viewportHeightInPixels / float(self.viewportWidthInPixels)
        else:
            viewportHeight = 2.0* viewportRadius
            viewportWidth = viewportHeight * self.viewportWidthInPixels / float(self.viewportHeightInPixels)

        left =  0.5 * viewportWidth
        right = - 0.5 * viewportWidth
        bottom = - 0.5 * viewportHeight
        top = 0.5 * viewportHeight

        print("left %s right %s top %s bottom %s" %(left, right, top, bottom))

        if jittered:
            if point:
                x_j = random.uniform(-.5,.5) * viewportWidth / self.viewportWidthInPixels
                y_j = random.uniform(-.5,.5) * viewportHeight / self.viewportHeightInPixels
            else:
                x_j = (point[0] - 0.5) * 0.5 * viewportWidth / self.viewportWidthInPixels
                y_j = (point[1] - 0.5) * 0.5 * viewportHeight / self.viewportHeightInPixels

            left += x_j
            right += x_j
            top += y_j
            bottom += y_j

        return Matrix44.perspective_projection_bounds(left, right, top, bottom, self.near_plane, self.far_plane)

    def getTransform(self):
        return Matrix44.look_at(self.position, self.target, -self.up)

    # Causes the camera to "orbit" around the target point.
    # This is also called "tumbling" in some software packages.
    def orbit(self,delta_x_pixels, delta_y_pixels):
        pixelsPerDegree = 1000 / float(self.orbiting_speed_degrees_per_radians)
        radiansPerPixel = 1.0 / pixelsPerDegree * math.pi / 180.0

        t2p = self.position - self.target

        M = Matrix4.rotationMatrix( - delta_x_pixels * radiansPerPixel, self.ground )
        t2p = M * t2p
        self.up = M * self.up
        
        right = (self.up.normalized() ^ t2p.normalized()).normalized()
        M = Matrix4.rotationMatrix( delta_y_pixels * radiansPerPixel, right )
        t2p = M * t2p
        self.up = M * self.up
        self.position = self.target + t2p

    # This causes the scene to appear to translate right and up
    # (i.e., what really happens is the camera is translated left and down).
    # This is also called "panning" in some software packages.
    # Passing in negative delta values causes the opposite motion.
    def pan( self, delta_x_pixels, delta_y_pixels ):
        direction = self.target - self.position
        distanceFromTarget = direction.length()
        direction = direction.normalized()

        translationSpeedInUnitsPerRadius = distanceFromTarget * math.tan( self.fov_degrees/2.0 / 180.0 * math.pi )
        pixelsPerUnit = self.viewportRadiusInPixels / translationSpeedInUnitsPerRadius

        right = direction ^ self.up

        translation = right*(- delta_x_pixels / pixelsPerUnit) + self.up*(- delta_y_pixels / pixelsPerUnit)

        self.position = self.position + translation
        self.target = self.target + translation

    # This causes the camera to translate forward into the scene.
    # This is also called "dollying" or "tracking" in some software packages.
    # Passing in a negative delta causes the opposite motion.
    # If ``push_target_distance'' is True, the point of interest translates forward (or backward)
    # *with* the camera, i.e. it's "pushed" along with the camera; otherwise it remains stationary.
    def dolly( self, delta_pixels, push_target_distance = None):
        direction = self.target - self.position
        distanceFromTarget = direction.length()
        direction = direction.normalized()

        translationSpeedInUnitsPerRadius = distanceFromTarget * math.tan( self.fov_degrees/2.0 / 180.0 * math.pi )
        pixelsPerUnit = self.viewportRadiusInPixels / translationSpeedInUnitsPerRadius

        dollyDistance = delta_pixels / pixelsPerUnit

        if not push_target_distance:
            distanceFromTarget -= dollyDistance
            if distanceFromTarget < self.target_push_threshold * self.near_plane:
                distanceFromTarget = self.target_push_threshold * self.near_plane

        self.position += direction * dollyDistance
        self.target = self.position + direction * distanceFromTarget

    def getBackgroundImageName(self):
        return ""