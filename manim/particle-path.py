from manim import *
import numpy as np

class ParticlePath(ThreeDScene):

    def construct(self):
        AXIS_CONFIG = {
            "x_range": [-1,1,0.25],
            "y_range": [-1,1,0.25],
            "z_range": [-1,1,0.25],
            "x_length": 5,
            "y_length":5,
            "z_length":4,
            "tips": False
        }

        axes_3d = ThreeDAxes(**AXIS_CONFIG)


        __x = lambda t: np.sin(t)
        __y = lambda t: np.cos(t)
        __z = lambda t: np.cos(2*t)

        __dx = lambda t: np.cos(t)
        __dy = lambda t: -np.sin(t)
        __dz = lambda t: -2*np.sin(2*t)

        __t = ValueTracker(0)

        func = ParametricFunction(
            lambda t: np.array([__x(t), __y(t), __z(t)]),
            t_range=(0,TAU),
            color=RED
        )

        pos = always_redraw(
            lambda: Arrow(start=axes_3d.coords_to_point(0,0,0), end=axes_3d.coords_to_point(__x(__t.get_value()), __y(__t.get_value()), __z(__t.get_value())))
        )

        self.set_camera_orientation(phi=45*DEGREES, theta=45*DEGREES, zoom=2)
        self.add(func, axes_3d, pos)
        self.play(__t.animate.set_value(TAU), rate_func=linear)