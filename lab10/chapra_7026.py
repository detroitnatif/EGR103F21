#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:48:18 2021

@author: tylerklimas
[chapra_7026.py]
[Tyler Klimas]
[11-20-21]

Using Egr93's "Lab 9 common code"

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as axes3d

def fun(x, y):
    return 4*x + 2*y + x**2 - 2*x**4 + 2*x*y - 3*y**2

min_v = opt.fmin(lambda vec: -1*fun(vec[0], vec[1]), [-10, 10])

min_l = fun(*min_v)

print('{:.3e}'.format(min_v[0]), '{:.3e}'.format(min_v[1]), '{:.3e}'.format(min_l))

x1 = np.linspace(-4, 4, 20)
y1 = np.linspace(-4, 4, 20)
x2, y2 = np.meshgrid(x1, y1)
z = fun(x2, y2)


min_l = fun(*min_v)


print('{:.3e}'.format(min_v[0]), '{:.3e}'.format(min_v[1]), '{:.3e}'.format(min_l))

sphere = plt.figure(num=1, clear=True)
splot = sphere.add_subplot(1, 1, 1, projection='3d')

num1 = splot.plot_wireframe(x2, y2, z, color = 'm')

sphere.savefig('7.026.png')