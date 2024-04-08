from manim import *
import numpy as np

class Hemisphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=-65*DEGREES, zoom=4)

        hemisphere = Surface(
            lambda u, v: np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v)]),
            u_range = (0,TAU),
            v_range = (0,TAU/4),
            resolution= (100,100)
        )

        # self.add(hemisphere)
        plane = Surface(
            lambda u, v: np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), 0]),
            u_range = (0,TAU),
            v_range = (0,TAU/4),
            resolution= (100,100)
        )
        
        self.play(ReplacementTransform(hemisphere, plane))
        self.play(ReplacementTransform(plane, Surface(
            lambda u, v: np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v)]),
            u_range = (0,TAU),
            v_range = (0,TAU/4),
            resolution= (100,100)
        )))


        