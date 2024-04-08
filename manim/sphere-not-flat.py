from manim import *
import numpy as np

class SphereNotHomeo(ThreeDScene):
    def construct(self):
        
        sphere = Surface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_range=(0,TAU),u_range=(-PI/2,PI/2),checkerboard_colors=[TEAL_D, TEAL_E],fill_opacity=0.50,
            resolution=(100,100)).scale(2)
        ellipsoid = Surface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_range=(0,TAU),u_range=(-PI/2,PI/2),checkerboard_colors=[TEAL_D, TEAL_E],fill_opacity=0.50,
            resolution=(100,100)).scale(2)
        
        ellipsoid_squish = Surface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.25*np.sin(u)
            ]),v_range=(0,TAU),u_range=(-PI/2,PI/2),checkerboard_colors=[TEAL_D, TEAL_E],fill_opacity=0.50,
            resolution=(100,100)).scale(2)
        
        ellipsoid_more_squish = Surface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.15*np.sin(u)
            ]),v_range=(0,TAU),u_range=(-PI/2,PI/2),checkerboard_colors=[TEAL_D, TEAL_E],fill_opacity=0.50,
            resolution=(100,100)).scale(2)
        
        ellipsoid_lateral_squish = Surface(
            lambda u, v: np.array([
                0.5*np.cos(u)*np.cos(v),
                0.5*np.cos(u)*np.sin(v),
                np.sin(u)
            ]),v_range=(0,TAU),u_range=(-PI/2,PI/2),checkerboard_colors=[TEAL_D, TEAL_E],fill_opacity=0.50,
            resolution=(100,100)).scale(2)
        
        self.set_camera_orientation(phi=90*DEGREES, zoom=0.75)
        
        self.begin_ambient_camera_rotation(rate=0.3)

        self.play(ReplacementTransform(sphere, ellipsoid))
        self.play(ReplacementTransform(ellipsoid, ellipsoid_squish))
        self.play(ReplacementTransform(ellipsoid_squish, ellipsoid_more_squish))
        self.play(ReplacementTransform(ellipsoid_more_squish, ellipsoid_lateral_squish))
        self.play(ReplacementTransform(ellipsoid_lateral_squish, Surface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_range=(0,TAU),u_range=(-PI/2,PI/2),checkerboard_colors=[TEAL_D, TEAL_E],fill_opacity=0.50,
            resolution=(100,100)).scale(2)))