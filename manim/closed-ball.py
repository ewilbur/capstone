from manim import *
import numpy as np


class ShrinkingCircle(Circle):
    def __init__(self, **kwards):
        super().__init__(**kwargs)

    def set_radius(self, radius):
        self.radius = radius
        self.refresh_parameters()

class ClosedBall(Scene):
    def construct(self):
        ball_radius = 2
        dash_circle = Circle(radius=ball_radius, color = BLACK)

        origin_coordinates = dash_circle.get_center()

        dotty = Dot(color = RED).move_to(origin_coordinates)
        neighborhood = Circle(radius=ball_radius/2).move_to(origin_coordinates)

        vg = VGroup()
        vg.add(dotty)
        vg.add(neighborhood)

        vg.shift(RIGHT*2)

        self.add(dash_circle, dotty, neighborhood)

        vg.generate_target()
        vg.target.scale(0.01)
        self.play(MoveToTarget(vg))
        vg.target.scale(1/0.01)
        self.play(MoveToTarget(vg))

        #self.play(MoveToTarget(vg, np.array([0,1])))

        # vg.generate_target()
        # vg.target.shift(RIGHT + UP).scale(0.4)
        # self.play(MoveToTarget(vg))

        # vg.target.shift(DOWN).scale((1/0.4)*0.85)
        # self.play(MoveToTarget(vg))

        # vg.target.shift(DOWN).scale((1/0.85)*0.4)
        # self.play(MoveToTarget(vg))

        # vg.target.shift(LEFT + UP).scale(1/0.4)
        # self.play(MoveToTarget(vg))

        # vg.target.shift(LEFT + UP).scale(0.4)
        # self.play(MoveToTarget(vg))

        # vg.target.shift(RIGHT + DOWN).scale(1/0.4)
        # self.play(MoveToTarget(vg))
