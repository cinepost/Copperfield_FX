import math
from OpenGL.GL import *

from copper.vmath import Matrix4, Vector3

class Camera(object):
    def __init__(self, position=[5,5,5], target=[0,0,0], fov_degrees = 45.0, near_plane = 0.1, far_plane = 1000.0):
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

    def buildFrustum(self):
        tangent = math.tan( self.fov_degrees/2.0 / 180.0 * math.pi )
        viewportRadius = self.near_plane * tangent
        if self.viewportWidthInPixels < self.viewportHeightInPixels:
            viewportWidth = 2.0*viewportRadius
            viewportHeight = viewportWidth * self.viewportHeightInPixels / float(self.viewportWidthInPixels)
        else:
            viewportHeight = 2.0*viewportRadius
            viewportWidth = viewportHeight * self.viewportWidthInPixels / float(self.viewportHeightInPixels)

        glFrustum(
            - 0.5 * viewportWidth,  0.5 * viewportWidth,    # left, right
            - 0.5 * viewportHeight, 0.5 * viewportHeight,   # bottom, top
            self.near_plane, self.far_plane
        )

    def getTransform(self):
        return Matrix4.lookAt(self.position, self.target, self.up, False)

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