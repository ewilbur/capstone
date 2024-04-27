from manim import *
import numpy as np

class ParticlePath(ThreeDScene):

    def construct(self):
        def TexVector(x,y,z):
            return r'\begin{pmatrix}' + "{:.2f}".format(x) + r'\\' + "{:.2f}".format(y) + r'\\' + "{:.2f}".format(z) + r'\end{pmatrix}'
        
        AXIS_CONFIG = {
            "x_range": [-1,1,0.25],
            "y_range": [-1,1,0.25],
            "z_range": [-1,1,0.25],
            "x_length": 5,
            "y_length":5,
            "z_length":4,
            "tips": False
        }

        axes = ThreeDAxes(**AXIS_CONFIG)


        __x = lambda t: np.sin(t)
        __y = lambda t: np.cos(t)
        __z = lambda t: np.cos(2*t)

        __dx = lambda t: np.cos(t)
        __dy = lambda t: -np.sin(t)
        __dz = lambda t: -2*np.sin(2*t)


        path = ParametricFunction(
            lambda t: np.array([__x(t), __y(t), __z(t)]),
            t_range=(0,TAU),
            color=PURPLE
        )

        __t = ValueTracker(0)

        
        dotty = always_redraw(
            lambda: Dot(radius=0).move_to(np.array([__x(__t.get_value()), __y(__t.get_value()), __z(__t.get_value())]))
        )

        #update_f = lambda mob: mob.put_start_and_end_on(start=ORIGIN, end=np.array([__x(__t.get_value()), __y(__t.get_value()), __z(__t.get_value())]))
        
        def updtr(mob):
            mob.put_start_and_end_on(start=ORIGIN, end=np.array([__x(__t.get_value()), __y(__t.get_value()), __z(__t.get_value())]))
        
        def terry_up(mob):
            mob.put_start_and_end_on(start=dotty.get_center(), end=dotty.get_center() + (1/np.sqrt(1 + 4*np.sin(2*__t.get_value())**2))*np.array([__dx(__t.get_value()),__dy(__t.get_value()),__dz(__t.get_value())]))

        arry = Arrow(stroke_width=0.30,max_tip_length_to_length_ratio=0.1,color=BLACK)
        arry.add_updater(updtr)

        tarry = Arrow(stroke_width=0.60,max_tip_length_to_length_ratio=0.1,color=BLACK)
        tarry.add_updater(terry_up)

        

        self.set_camera_orientation(phi=45*DEGREES, theta=45*DEGREES, zoom=2)
        self.begin_ambient_camera_rotation(rate=-1)
        self.add(path, dotty, arry, tarry)
        self.play(__t.animate.set_value(TAU), rate_func = linear, run_time=5)



class ParticlePathTex(Scene):
    def construct(self):
        def TexVector(x,y,z):
            return r'\begin{pmatrix}' + "{:.2f}".format(x) + r'\\' + "{:.2f}".format(y) + r'\\' + "{:.2f}".format(z) + r'\end{pmatrix}'
 
        __x = lambda t: np.sin(t)
        __y = lambda t: np.cos(t)
        __z = lambda t: np.cos(2*t)

        __dx = lambda t: np.cos(t)
        __dy = lambda t: -np.sin(t)
        __dz = lambda t: -2*np.sin(2*t)

        __t = ValueTracker(0)
        path_tex = always_redraw(
            lambda: MathTex('f = ' + TexVector(__x(__t.get_value()), __y(__t.get_value()), __z(__t.get_value())),color=BLACK).move_to(UP)
        )

        tangent_tex = always_redraw(
            lambda: MathTex('f\' = ' + TexVector(__dx(__t.get_value()), __dy(__t.get_value()), __dz(__t.get_value())),color=BLACK).move_to(DOWN)
        )

        self.add(path_tex, tangent_tex)
        self.play(__t.animate.set_value(TAU), rate_func=linear, run_time=5)
        pass 