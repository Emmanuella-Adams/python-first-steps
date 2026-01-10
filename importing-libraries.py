#Let's say that you want to import the math module. In that case, you would write this at the top of your file:

import pandas as pd
from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978

#if you want tp import everything from the library, you use

from math import *

#if you want the code to run only if it is the main program, you do this
if __name__ == '__main__': 
    print(f'ood')