from manim import *
import numpy as np

class Paraboloid(ThreeDScene):
    def construct(self):
        steps = 1

        paraboloid = Surface(
            lambda u, v: np.array([u, v, u**2 + v**2]),
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

        self.play(ReplacementTransform(paraboloid, plane))
        self.play(ReplacementTransform(plane,Surface(
            lambda u, v: np.array([u, v, u**2 + v**2]),
            u_range=(-1.5,1.5),
            v_range=(-1.35,1.35),
            resolution=(100,100),
            )))

        # self.play(ReplacementTransform(Surface(
        #         lambda u, v: np.array([u, v, u**2 + v**2]),
        #         u_range=(-1.5,1.5),
        #         v_range=(-1.35,1.35),
        #         resolution=(10,10),
        #         ), Surface(
        #             lambda u, v: np.array([u,v,0]),
        #             u_range=(-1.5,1.5),
        #             v_range=(-1.35,1.35),
        #             resolution=(10,10),
        #         )))
    
        # self.play(ReplacementTransform(Surface(
        #             lambda u, v: np.array([u,v,0]),
        #             u_range=(-1.5,1.5),
        #             v_range=(-1.35,1.35),
        #             # resolution=(100,100),
        #         ),Surface(
        #         lambda u, v: np.array([u, v, u**2 + v**2]),
        #         u_range=(-1.5,1.5),
        #         v_range=(-1.35,1.35),
        #         # resolution=(100,100),
        #         )))
        # first_iteration = True
        # for t in range(steps)[::-1]:
        #     if first_iteration:
        #         paraboloid = Surface(
        #         lambda u, v: np.array([u, v, u**2 + v**2]),
        #         u_range=(-1.5,1.5),
        #         v_range=(-1.35,1.35)
        #         )
        #         first_iteration = False
        #     s2 = Surface(
        #         lambda u, v: np.array([u, v, (u**2 + v**2)*(t/steps)]),
        #         u_range=(-1.5,1.5),
        #         v_range=(-1.35,1.35)
        #     )
        #     self.play(ReplacementTransform(paraboloid, s2))
        #     paraboloid = s2

        #     for t in range(steps):
        #         if first_iteration:
        #             paraboloid = Surface(
        #             lambda u, v: np.array([u, v, (u**2 + v**2)]),
        #             u_range=(-1.5,1.5),
        #             v_range=(-1.35,1.35)
        #             )
        #             first_iteration = False
        #         s2 = Surface(
        #             lambda u, v: np.array([u, v, (u**2 + v**2)*(t/steps)]),
        #             u_range=(-1.5,1.5),
        #             v_range=(-1.35,1.35)
        #         )
        #         self.play(ReplacementTransform(paraboloid, s2))
        #         paraboloid = s2