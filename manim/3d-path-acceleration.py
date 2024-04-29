from manim import *
import numpy as np

class ThreeDPathAcceleration(ThreeDScene):
    def construct(self):
        R = 2
        r = 1
        __f = lambda t: np.cos(8*t)
        __g = lambda t: t

        __x = lambda t: np.sin(t)
        __y = lambda t: np.cos(t)
        __z = lambda t: np.cos(2*t)

        __dx = lambda t: -(8*np.cos(2*t)*np.cos(t)*np.sin(2*t)/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) + np.sin(t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))/((8*np.cos(2*t)*np.cos(t)*np.sin(2*t)/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) + np.sin(t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))**2 + 16*(4*np.cos(2*t)*np.sin(2*t)**2/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) - np.cos(2*t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))**2 + (8*np.cos(2*t)*np.sin(2*t)*np.sin(t)/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) - np.cos(t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))**2)
        __dy = lambda t: (8*np.cos(2*t)*np.sin(2*t)*np.sin(t)/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) - np.cos(t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))/((8*np.cos(2*t)*np.cos(t)*np.sin(2*t)/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) + np.sin(t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))**2 + 16*(4*np.cos(2*t)*np.sin(2*t)**2/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) - np.cos(2*t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))**2 + (8*np.cos(2*t)*np.sin(2*t)*np.sin(t)/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) - np.cos(t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))**2)
        __dz = lambda t:4*(4*np.cos(2*t)*np.sin(2*t)**2/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) - np.cos(2*t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))/((8*np.cos(2*t)*np.cos(t)*np.sin(2*t)/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) + np.sin(t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))**2 + 16*(4*np.cos(2*t)*np.sin(2*t)**2/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) - np.cos(2*t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))**2 + (8*np.cos(2*t)*np.sin(2*t)*np.sin(t)/(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2)**(3/2) - np.cos(t)/np.sqrt(np.cos(t)**2 + 4*np.sin(2*t)**2 + np.sin(t)**2))**2)
        pathy = ParametricFunction(
            lambda t: np.array([__x(t), __y(t), __z(t)]),
            t_range=(0,TAU),
            color=GREEN
        )

        __t = ValueTracker(0)
        def mag(x):
            return np.sqrt(np.dot(x,x))
        
        arry = Arrow(color=PURPLE)
        arry = always_redraw(
            lambda: arry.put_start_and_end_on(
                start=np.array([__x(__t.get_value()), __y(__t.get_value()), __z(__t.get_value())]),
                end=(np.array([__x(__t.get_value()), __y(__t.get_value()), __z(__t.get_value())]) + (0.75/(mag(np.array([__dx(__t.get_value()), __dy(__t.get_value()), __dz(__t.get_value())])))**2)*(np.array([__dx(__t.get_value()), __dy(__t.get_value()), __dz(__t.get_value())]))),
            )
        )

        self.add(pathy, arry)        
        self.set_camera_orientation(phi=45*DEGREES, zoom=2)
        self.begin_ambient_camera_rotation(rate=-1)
        self.play(__t.animate.set_value(TAU), rate_func=linear, run_time=TAU)