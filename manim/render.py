#!/bin/python3
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

os.system('cmd /c docker run -v ' + dir_path + ':/manim manim-sage manim ' + ' '.join(sys.argv[1:]))