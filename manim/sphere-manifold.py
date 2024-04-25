from manim import *
import numpy as np

class SphereManifold(ThreeDScene):
    def construct(self):

        res = (100,100)
        hemisphereL = Surface(
            lambda u, v: np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v)]),
            u_range = (0,TAU),
            v_range = (0,TAU/3.5),
            resolution= res,
            fill_opacity=0.35,
            fill_color = RED
        ).shift(LEFT*5)

        sphereL = Surface(
            lambda u, v: np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v)]),
            u_range = (0,TAU),
            v_range = (0,TAU/2),
            resolution= res,
            fill_opacity=0.15
        )

        planeL = Surface(
            lambda u, v: np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), 0]),
            u_range = (0, TAU),
            v_range = (0, TAU/4),
            resolution = res,
            fill_opacity = 0.35,
            fill_color = RED
        ).shift(LEFT * 8)

        planeR = Surface(
            lambda u, v: np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), 0]),
            u_range = (0, TAU),
            v_range = (0, TAU/4),
            resolution = res,
            fill_opacity = 0.35,
            fill_color = PURPLE
        ).shift(RIGHT * 5)

        hemisphereR = Surface(
            lambda u, v: np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), -np.cos(v)]),
            u_range = (0,TAU),
            v_range = (0,TAU/3.5),
            resolution= res,
            fill_opacity=0.35,
            fill_color = PURPLE
        ).shift(RIGHT*4)

        sphereR = Surface(
            lambda u, v: np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), -np.cos(v)]),
            u_range = (0,TAU),
            v_range = (0,TAU/2),
            resolution= res,
            fill_opacity=0.15
        )

        sphere = Surface(
            lambda u, v: np.array([np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v)]),
            u_range = (0,TAU),
            v_range = (0,TAU/2),
            resolution= res,
            fill_opacity=1,
            fill_color = GREEN
        ) 

        self.set_camera_orientation(phi=65*DEGREES, theta=0*DEGREES, gamma=90*DEGREES, zoom=1.75)
        # self.add(planeR, hemisphereR, sphere)

        self.add(sphere)
        self.play(Write(planeR), Write(planeL))
        self.play(ReplacementTransform(planeR, hemisphereR), ReplacementTransform(planeL, hemisphereL))
        self.play(ReplacementTransform(hemisphereR, sphereR), ReplacementTransform(hemisphereL, sphereL))
        self.wait()
        
        