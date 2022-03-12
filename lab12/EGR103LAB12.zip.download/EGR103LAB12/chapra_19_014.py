#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tylerklimas
[chapra6.16.py]
[Tyler Klimas]
[11-29-21]


I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.interpolate import interp2d 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def fun(x, y):
    t = 2 + x - y + 2*x**2 + 2*x*y + y**2
    return t

x = np.linspace(-2, 0, 9)
y = np.linspace(0,3,9)

x1, y1 = np.meshgrid(x, y)

t1 = fun(x1, y1)

tinterp = interp2d(x, y, t1, kind='linear')
spline = interp2d(x, y, t1, kind = 'cubic')

real = fun(-1.63, 1.627)
print(real)
pred = tinterp(-1.63, 1.627)[0]
print(pred)

per = ((pred - real)/real) * 100
print(per)

pred2 = spline(-1.63, 1.627)[0]
print(pred2)

per2 = abs(((pred2 - real)/real) * 100)
print(per2)


