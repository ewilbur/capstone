from manim import *
import numpy as np

class PathAcceleration(Scene):
    def construct(self):
        R = 5
        r = 3
        d = 5
        x = lambda t: (1/2)*((R - r)*np.cos(t) + d*np.cos(((R-r)/r)*t))
        y = lambda t: (1/2)*((R - r)*np.sin(t) - d*np.sin(((R-r)/r)*t))
        z = lambda t: 0

        dx = lambda t: -4/9*(607500*(2*np.cos(2/3*t)**3 - np.cos(2/3*t))*np.sin(2/3*t)*np.sin(t)**5 + 253125*np.cos(2/3*t)**5 + 10125*(200*np.cos(2/3*t)**5 - 88*np.cos(2/3*t)**3 - 15*(8*np.cos(2/3*t)**4 - 8*np.cos(2/3*t)**2 + 1)*np.cos(t) - 59*np.cos(2/3*t))*np.sin(t)**4 + 2700*(15*(50*np.cos(2/3*t)**4 + 3*np.cos(2/3*t)**2 - 7)*np.cos(t)*np.sin(2/3*t) - (1375*np.cos(2/3*t)**3 - 553*np.cos(2/3*t))*np.sin(2/3*t))*np.sin(t)**3 - 60750*np.cos(2/3*t)**3 - 90*(22500*np.cos(2/3*t)**5 - 8775*np.cos(2/3*t)**3 - 15*(2300*np.cos(2/3*t)**4 - 2031*np.cos(2/3*t)**2 + 153)*np.cos(t) - 13139*np.cos(2/3*t))*np.sin(t)**2 - 3*(208125*np.cos(2/3*t)**4 - 444550*np.cos(2/3*t)**2 - 112999)*np.cos(t) - 60*(3*(5625*np.cos(2/3*t)**4 + 900*np.cos(2/3*t)**2 - 3757)*np.cos(t)*np.sin(2/3*t) - 10*(3375*np.cos(2/3*t)**3 - 2567*np.cos(2/3*t))*np.sin(2/3*t))*np.sin(t) - 1241255*np.cos(2/3*t))/((3375*(4*np.cos(2/3*t)**2 - 1)*np.sin(2/3*t)*np.sin(t)**3 - 225*(58*np.cos(2/3*t)**2 + 15*(4*np.cos(2/3*t)**3 - 3*np.cos(2/3*t))*np.cos(t) - 29)*np.sin(t)**2 + 6525*np.cos(2/3*t)**2 + 15*(225*np.cos(2/3*t)**3 - 253*np.cos(2/3*t))*np.cos(t) - 15*(870*np.cos(2/3*t)*np.cos(t)*np.sin(2/3*t) + (675*np.cos(2/3*t)**2 - 253)*np.sin(2/3*t))*np.sin(t) - 8993)*(-10/3*np.cos(2/3*t)*np.cos(t) + 10/3*np.sin(2/3*t)*np.sin(t) + 34/9)**(3/2))
        dy = lambda t: 4/9*(151875*(8*np.cos(2/3*t)**4 - 8*np.cos(2/3*t)**2 + 1)*np.sin(t)**5 + 10125*(60*(2*np.cos(2/3*t)**3 - np.cos(2/3*t))*np.cos(t)*np.sin(2/3*t) + (200*np.cos(2/3*t)**4 - 312*np.cos(2/3*t)**2 + 53)*np.sin(2/3*t))*np.sin(t)**4 + 1350*(500*np.cos(2/3*t)**4 - 769*np.cos(2/3*t)**2 - 30*(50*np.cos(2/3*t)**5 - 103*np.cos(2/3*t)**3 + 46*np.cos(2/3*t))*np.cos(t) + 197)*np.sin(t)**3 - 300*(1575*np.cos(2/3*t)**3 - 3757*np.cos(2/3*t))*np.cos(t)*np.sin(2/3*t) + 90*(30*(475*np.cos(2/3*t)**3 - 372*np.cos(2/3*t))*np.cos(t)*np.sin(2/3*t) - (22500*np.cos(2/3*t)**4 - 33975*np.cos(2/3*t)**2 + 11339)*np.sin(2/3*t))*np.sin(t)**2 + 5*(50625*np.cos(2/3*t)**4 - 68850*np.cos(2/3*t)**2 - 112999)*np.sin(2/3*t) - 3*(421875*np.cos(2/3*t)**4 - 779350*np.cos(2/3*t)**2 - 60*(5625*np.cos(2/3*t)**5 - 11025*np.cos(2/3*t)**3 + 7582*np.cos(2/3*t))*np.cos(t) + 488699)*np.sin(t))/((3375*(4*np.cos(2/3*t)**2 - 1)*np.sin(2/3*t)*np.sin(t)**3 - 225*(58*np.cos(2/3*t)**2 + 15*(4*np.cos(2/3*t)**3 - 3*np.cos(2/3*t))*np.cos(t) - 29)*np.sin(t)**2 + 6525*np.cos(2/3*t)**2 + 15*(225*np.cos(2/3*t)**3 - 253*np.cos(2/3*t))*np.cos(t) - 15*(870*np.cos(2/3*t)*np.cos(t)*np.sin(2/3*t) + (675*np.cos(2/3*t)**2 - 253)*np.sin(2/3*t))*np.sin(t) - 8993)*(-10/3*np.cos(2/3*t)*np.cos(t) + 10/3*np.sin(2/3*t)*np.sin(t) + 34/9)**(3/2))
        dz = lambda t: 0
        pathy = ParametricFunction(
            lambda t: np.array([x(t),y(t),z(t)]),
            t_range = (0,3*TAU),
            color=GREEN
        )

        __t = ValueTracker(0)

        def mag(x):
            return np.sqrt(np.dot(x,x))

        dotty = Dot()
        arry = Arrow(color=PURPLE)
        arry = always_redraw(
            lambda: arry.put_start_and_end_on(
                start=np.array([x(__t.get_value()), y(__t.get_value()), 0]),
                end=(np.array([x(__t.get_value()), y(__t.get_value()), 0]) + (2/(mag(np.array([dx(__t.get_value()), dy(__t.get_value()), 0])))**2)*(np.array([dx(__t.get_value()), dy(__t.get_value()), 0]))),
            )
        )

        self.add(pathy, arry)
        self.play(__t.animate.set_value(3*TAU), rate_func=linear, run_time=10)