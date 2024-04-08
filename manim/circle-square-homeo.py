from manim import *
import numpy as np

class Homeo(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=0.5)
        # self.play(DrawBorderThenFill(square))
        #self.add(square)
        circle = Circle(color=GREEN, fill_opacity=0.5)
        pentagon = RegularPolygon(n=5, color=TEAL, fill_opacity=0.5)
        octogon = RegularPolygon(n=8, color=PURPLE, fill_opacity=0.5)
        triangle = RegularPolygon(n=3, color=RED, fill_opacity=0.5)

        # self.add(square)
        self.play(ReplacementTransform(square, circle))
        # self.play(Indicate(circle))
        self.play(ReplacementTransform(circle, pentagon))
        # # self.play(Indicate(pentagon))
        self.play(ReplacementTransform(pentagon, octogon))
        # # self.play(Indicate(octogon))
        self.play(ReplacementTransform(octogon, triangle))
        # # self.play(Indicate(triangle))
        self.play(ReplacementTransform(triangle, Square(color=BLUE, fill_opacity=0.5)))
        
        
        #self.play(Indicate(square))
        # self.play(FadeOut(pentagon))