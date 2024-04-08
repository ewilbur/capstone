from manim import *
import numpy as np

class CircleDot(Scene):
    def construct(self):
        circle = Circle(radius=2, color=PURPLE)
        arcL = Arc(angle=TAU/10, color=BLACK).rotate(angle=300*DEGREES).move_to(2*RIGHT*np.cos(np.pi/4) + 2*UP*np.sin(np.pi/4))
        arcR = Arc(angle=TAU/10, color=BLACK).rotate(angle=120*DEGREES).move_to(2*RIGHT*np.cos(np.pi/3) + 2*UP*np.sin(np.pi/3))

        vg = VGroup()
        vg.add(arcL, arcR, circle)
        self.add(circle, arcL, arcR)

        vg.generate_target()
        vg.target.scale(0.01)
        self.play(MoveToTarget(vg))
        vg.target.scale(1/0.01)
        self.play(MoveToTarget(vg))