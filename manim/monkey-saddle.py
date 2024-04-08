from manim import *
import numpy as np

class MonkeySaddle(ThreeDScene):
    def construct(self):

        monkey = Surface(
            lambda u, v: np.array([u, v, ((u**3) - 3*u*(v**2))]),
            u_range=(-1.5,1.5),
            v_range=(-1.35,1.35),
            resolution=(100,100),
            )
        plane = Surface(
                    lambda u, v: np.array([u,v,0]),
                    u_range=(-1.5,1.5),
                    v_range=(-1.35,1.35),
                    resolution=(100,100),
                )

        self.set_camera_orientation(phi=65*DEGREES, theta=-65*DEGREES, zoom=0.75)

        self.play(ReplacementTransform(monkey, plane))
        self.play(ReplacementTransform(plane,Surface(
            lambda u, v: np.array([u, v, ((u**3) - 3*u*(v**2))]),
            u_range=(-1.5,1.5),
            v_range=(-1.35,1.35),
            resolution=(100,100),
            )))



# from manim import *
# import numpy as np

# class MonkeySaddle(ThreeDScene):
#     def construct(self):
#         saddle = None
#         steps = 5

#         self.set_camera_orientation(phi=65*DEGREES, theta=-65*DEGREES, zoom=0.75)
#         # self.add(Surface(
#         #         lambda u, v: np.array([u, v, ((u**3) - 3*u*(v**2))]),
#         #         u_range=(-1.5,1.5),
#         #         v_range=(-1.35,1.35)
#         #         ))

#         first_iteration = True
#         for t in range(steps)[::-1]:
#             if first_iteration:
#                 saddle = Surface(
#                 lambda u, v: np.array([u, v, ((u**3) - 3*u*(v**2))]),
#                 u_range=(-1.5,1.5),
#                 v_range=(-1.35,1.35)
#                 )
#                 first_iteration = False
#             s2 = Surface(
#                 lambda u, v: np.array([u, v, ((u**3) - 3*u*(v**2))*(t/steps)]),
#                 u_range=(-1.5,1.5),
#                 v_range=(-1.35,1.35)
#             )
#             self.play(ReplacementTransform(saddle, s2))
#             saddle = s2

#             for t in range(steps):
#                 if first_iteration:
#                     saddle = Surface(
#                     lambda u, v: np.array([u, v, ((u**3) - 3*u*(v**2))]),
#                     u_range=(-1.5,1.5),
#                     v_range=(-1.35,1.35)
#                     )
#                     first_iteration = False
#                 s2 = Surface(
#                     lambda u, v: np.array([u, v, ((u**3) - 3*u*(v**2))*(t/steps)]),
#                     u_range=(-1.5,1.5),
#                     v_range=(-1.35,1.35)
#                 )
#                 self.play(ReplacementTransform(saddle, s2))
#                 saddle = s2