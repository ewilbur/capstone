from manim import *
import numpy as np


class ShrinkingCircle(Circle):
    def __init__(self, **kwards):
        super().__init__(**kwargs)

    def set_radius(self, radius):
        self.radius = radius
        self.refresh_parameters()

class OpenBall(Scene):
    def construct(self):
        ball_radius = 2
        dash_circle = DashedVMobject(
            Circle(radius=ball_radius, color = BLACK), 
            num_dashes = 20,
            dashed_ratio = 0.35,
            equal_lengths = True,
            )

        origin_coordinates = dash_circle.get_center()

        dotty = Dot(color = RED).move_to(origin_coordinates)
        neighborhood = Circle(radius=ball_radius/2).move_to(origin_coordinates)

        vg = VGroup()
        vg.add(dotty)
        vg.add(neighborhood)


        self.add(dash_circle, dotty, neighborhood)

        #self.play(MoveToTarget(vg, np.array([0,1])))

        vg.generate_target()
        vg.target.shift(RIGHT + UP).scale(0.4)
        self.play(MoveToTarget(vg))

        vg.target.shift(DOWN).scale((1/0.4)*0.85)
        self.play(MoveToTarget(vg))

        vg.target.shift(DOWN).scale((1/0.85)*0.4)
        self.play(MoveToTarget(vg))

        vg.target.shift(LEFT + UP).scale(1/0.4)
        self.play(MoveToTarget(vg))

        vg.target.shift(LEFT + UP).scale(0.4)
        self.play(MoveToTarget(vg))

        vg.target.shift(RIGHT + DOWN).scale(1/0.4)
        self.play(MoveToTarget(vg))
