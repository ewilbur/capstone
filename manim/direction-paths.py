from manim import *
import numpy as np

class DirectionPath(Scene):
    def zig_zag(self, t):
        assert(t >= 0)
        if t <= TAU / 4:
            return (4/TAU)*t
        elif t <= (3*TAU)/4:
            return -(4/TAU)*(t - TAU/2)
        elif t <= TAU:
            return (4/TAU)*(t - TAU)
        else:
            while t > TAU:
                t -= TAU
            return self.zig_zag(t)
    def construct(self):

        zig_path = ParametricFunction(
            lambda t: np.array([t,t]),
            t_range = np.array([0,TAU])
        )
        pass