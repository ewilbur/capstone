from manim import *
import numpy as np

class Chart1(ThreeDScene):
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

        axes_2d = Axes(
            x_range= [-5,5,1],
            y_range= [-5,5,1],
            x_length=3,
            y_length=3,
            tips=False,
        )

        surface = Surface(
            lambda u, v: np.array([u, v, np.sin(u - v)]),
            u_range=(-2,2),
            v_range=(-2,2),
            fill_color=PURPLE,
            fill_opacity=1,
            stroke_color=PURPLE,
            stroke_opacity=1,
            #checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(100,100)
        )

        axes_3d = ThreeDAxes(**AXIS_CONFIG)


        axes_3d.shift(RIGHT*3)
        axes_2d.shift(LEFT*3)


        surface.move_to(axes_3d.coords_to_point(0,0,0))

        #circle = Circle(radius=1, color=GREEN).move_to(axes_2d.c2p(0,0))
#         surface_2d = Surface(
#             lambda u, v: np.array([u,v,0]),
#             u_range=(-1,1),
#             v_range=(-1,1),
# #            checkerboard_colors=[PURPLE_D, PURPLE_E],
#             resolution=(25,25)
#         )

 #       surface_2d.move_to(axes_2d.c2p(0,0))
  
        some_path = ParametricFunction(
            lambda t: np.array([np.sin(2*t), np.sin(3*t), 0]),
            t_range = np.array([0,TAU]),
            color = BLACK,
        ).move_to(axes_2d.c2p(0,0))



        some_path_3d = ParametricFunction(
            lambda t: np.array([np.sin(2*t) - 2, np.sin(3*t) + 2, np.sin(np.sin(2*t) - 2 - np.sin(3*t) + 2)]),
            t_range = np.array([0,TAU]),
            color = BLACK,
        ).move_to(axes_3d.coords_to_point(0,0,0))

        
        
        dot2d = Dot(color = RED).move_to(axes_2d.c2p(0,0))
        dot3d = Dot(color = RED).move_to(axes_3d.coords_to_point(0,0,0))

        text_chart = Text("Chart", color=BLACK).next_to(axes_2d, direction=UP)
        text_graph = Text("Surface", color=BLACK).next_to(axes_3d, direction=UP)

        self.add_fixed_in_frame_mobjects(text_chart, text_graph,axes_2d,some_path,dot2d)#,surface_2d)

        self.move_camera(phi=45*DEGREES, radius=20)

        self.add(axes_2d, axes_3d, surface, some_path, some_path_3d, dot2d, dot3d, text_chart, text_graph)

        self.play(MoveAlongPath(dot2d, some_path, run_time=TAU), MoveAlongPath(dot3d, some_path_3d, run_time=TAU), rate_func=linear)