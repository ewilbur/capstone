from manim import *
import numpy as np

class Helicoid(ThreeDScene):
    def construct(self):
        AXIS_CONFIG = {
            "x_range": [-5,5,1],
            "y_range": [-5,5,1],
            "z_range": [-5,5,1],
            "x_length": 5,
            "y_length":5,
            "z_length":4,
            "tips": False
        }
        axes = ThreeDAxes(**AXIS_CONFIG)
        helicoid = Surface(
            lambda u, v: np.array([u*np.cos(v), u*np.sin(v), 0.5*v]),
            u_range=(-2,2),
            v_range=(-TAU,TAU),
            resolution=(100,100),
            fill_color=PURPLE,
            stroke_color=PURPLE
        )

        plane = Surface(
            lambda u, v: np.array([u, 0, v]),
            u_range=(-1.5,1.5),
            v_range=(-TAU/2,TAU/2)
        )

        self.set_camera_orientation(phi=45*DEGREES, radius=50)
        steps = 10
        for t in range(steps)[::-1]:
            s2 = Surface(
                lambda u, v: np.array([u*np.cos(v*(t)/steps), u*np.sin(v*(t)/steps), 0.5*v]),
                u_range=(-2,2),
                v_range=(-TAU,TAU),
                resolution=(100,100),
                fill_color=PURPLE,
                stroke_color=PURPLE
            )
            self.play(ReplacementTransform(helicoid, s2))
            helicoid = s2

        for t in range(steps):
            s2 = Surface(
                lambda u, v: np.array([u*np.cos(v*(t)/steps), u*np.sin(v*(t)/steps), 0.5*v]),
                u_range=(-2,2),
                v_range=(-TAU,TAU),
                fill_color=PURPLE,
                stroke_color=PURPLE,
                resolution=(100,100),
            )
            self.play(ReplacementTransform(helicoid, s2))
            helicoid = s2
        



        # self.add(helicoid)
        # #self.play(Write(helicoid))
        # self.wait()
        # self.play(ReplacementTransform(helicoid, plane))
        # self.wait()
        # self.play(ReplacementTransform(plane, Surface(
        #     lambda u, v: np.array([u*np.cos(v), u*np.sin(v), 0.5*v]),
        #     u_range=(-2,2),
        #     v_range=(-TAU,TAU)
        # )))
        # self.wait()