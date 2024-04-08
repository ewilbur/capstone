from manim import *
import numpy as np

class HyperbolicParaboloid(ThreeDScene):
    def construct(self):
        steps = 1

        paraboloid = Surface(
            lambda u, v: np.array([u, v, u**2 - v**2]),
            u_range=(-1.5,1.5),
            v_range=(-1.35,1.35),
            resolution=(100,100),
            )
        plane = Surface(
                    lambda u, v: np.array([u,v,0]),
                    u_range=(-1.5,1.5),
                    v_range=(-1.35,1.35),
                    resolution=(100,100),
                )

        self.set_camera_orientation(phi=65*DEGREES, theta=-65*DEGREES, zoom=0.75)

        self.play(ReplacementTransform(paraboloid, plane))
        self.play(ReplacementTransform(plane,Surface(
            lambda u, v: np.array([u, v, u**2 - v**2]),
            u_range=(-1.5,1.5),
            v_range=(-1.35,1.35),
            resolution=(100,100),
            )))