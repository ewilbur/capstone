from manim import *
import numpy as np
from sage.arith.misc import kronecker


class FrenetPath(ParametricFunction):
    @staticmethod
    def ZERO():
        return np.array([0,0,0])


    def __init__(self,f,t,n,b,speed,tau,kappa, **kwargs):
        self.__f = f
        self.__n = n
        self.__t = t
        self.__b = b
        self.__speed = speed
        self.__tau = tau
        self.__kappa = kappa

        super().__init__(f)

    def tangent(self):
        return self.__t
    
    def normal(self):
        return self.__n
    
    def binormal(self):
        return self.__b
    
    def velocity(self):
        return self.__speed * self.__t
    
    def curvature(self):
        return self.__kappa * self.__n
    
    def torsion(self):
        return self.__tau * self.__b


class CurvyPath(Scene):
    def construct(self):
        frenet = FrenetPath(
            lambda t: np.array([1/np.sqrt(np.cos(t)**2 + 1), np.cos(t)/np.sqrt(np.cos(t)**2 + 1), 0]),
            
        )
        pass

