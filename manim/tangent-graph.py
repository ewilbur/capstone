from manim import *
import numpy as np


class TangentGraph(Scene):
    def construct(self):
        scaled = DOWN * 1.75
        f = ParametricFunction(
            lambda t: np.array([t + scaled[0], t**2 + scaled[1], 0 + scaled[2]]),
            t_range=(-2,2),
            color=PURPLE,
        )

        self.play(Write(f))

        x = -2
        dist = 4
        num_tangent_lines = 10

        lns = [f]

        for i in range(num_tangent_lines):
            tngnt_line = ParametricFunction(
                lambda t: np.array([x + t + scaled[0],2*x*t + x**2 + scaled[1],0 + scaled[2]]),
                t_range=(-2,2),
                color=RED
            )
            lns.append(tngnt_line)
            self.play(Write(tngnt_line))
            x += dist / num_tangent_lines

        grp = VGroup(*lns)
        self.play(FadeOut(grp))
        pass