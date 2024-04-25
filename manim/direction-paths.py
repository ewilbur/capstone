from manim import *
import numpy as np


class DirectionPath(Scene):
    def zig_zag(self, t):
        if t < 0:
            return -self.zig_zag(-t)
        elif t <= TAU / 4:
            return (4/TAU)*t
        elif t <= (3*TAU)/4:
            return -(4/TAU)*(t - TAU/2)
        elif t <= TAU:
            return (4/TAU)*(t - TAU)
        else:
            while t > TAU:
                t -= TAU
            return self.zig_zag(t)
        
    def derivative_zig_zag(self, t):
        if t < 0:
            return self.derivative_zig_zag(-t)
        elif t <= TAU / 4:
            return (4/TAU)
        elif t <= (3*TAU)/4:
            return -(4/TAU)
        elif t <= TAU:
            return (4/TAU)
        else:
            while t > TAU:
                t -= TAU
            return self.zig_zag(t)

    def derivative_sin(self, t):
        return np.cos(t)
    


    def construct(self):

        rng = np.array([0, TAU])
        s = TAU/1.80

        zig_path = ParametricFunction(
            lambda t: np.array((t, self.zig_zag(t), 0)),
            t_range = rng,
            color = RED,
            use_smoothing = False
        ).move_to(LEFT*s)

        sin_path = ParametricFunction(
            lambda t: np.array((t, np.sin(t), 0)),
            t_range = rng,
            color = PURPLE
        ).move_to(RIGHT*s)

        zig_arr = Arrow(color=BLACK)
        zig_dot = Dot(color=GREEN).move_to(zig_path.get_left())

        sin_arr = Arrow(color=BLACK)
        sin_dot = Dot(color=BLUE).move_to(sin_path.get_left())

        def sin_dot_t():
            return (sin_dot.get_center() - sin_path.get_left())[0]
    

        def sin_arr_pos(dot):
            sin_arr_start = dot.get_center()
            sin_arr_slope = self.derivative_sin(sin_dot_t())
            sin_arr_magnitude = np.sqrt(1 + sin_arr_slope**2)
            sin_arr_dir = np.array([1/sin_arr_magnitude, sin_arr_slope/sin_arr_magnitude, 0])
            sin_arr_end = sin_arr_start + sin_arr_dir
            return sin_arr_start, sin_arr_end


        def sin_arr_updater(mob):
            sin_arr_start, sin_arr_end = sin_arr_pos(sin_dot)
            mob.put_start_and_end_on(start = sin_arr_start, end = sin_arr_end)

        def zig_dot_t():
            return (zig_dot.get_center() - zig_path.get_left())[0]
        
        def zig_arr_pos(dot):
            zig_arr_start = dot.get_center()
            zig_arr_slope = self.derivative_zig_zag(zig_dot_t())
            zig_arr_magnitude = np.sqrt(1 + zig_arr_slope**2)
            zig_arr_dir = np.array([1/zig_arr_magnitude, zig_arr_slope/zig_arr_magnitude, 0])
            zig_arr_end = zig_arr_start + zig_arr_dir
            return zig_arr_start, zig_arr_end
        
        def zig_arr_updater(mob):
            zig_arr_start, zig_arr_end = zig_arr_pos(zig_dot)
            mob.put_start_and_end_on(start = zig_arr_start, end = zig_arr_end)

        zig_arr.add_updater(zig_arr_updater)
        sin_arr.add_updater(sin_arr_updater)

        self.add(zig_path, zig_dot, zig_arr)
        self.add(sin_path, sin_dot, sin_arr)
        self.play(MoveAlongPath(zig_dot, zig_path, run_time=5), MoveAlongPath(sin_dot, sin_path, run_time=5))


        