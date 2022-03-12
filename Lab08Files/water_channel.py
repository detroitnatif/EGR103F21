#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:32:48 2021

@author: tylerklimas

[water_channel.py]
[Tyler Klimas]
[10-30-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]

"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as axes3d
from matplotlib import cm


nx = .02
sx = .001
bx, hx = np.meshgrid(np.linspace(.01, 20, 40), np.linspace(.01, 5, 41))


def manning(s, b, h, n):
    u = ((s**(1/2))/n)*(b*h/(b+2*h))**(2/3)
    return u
ux = manning(sx, bx, hx, nx)

mann_plot = plt.figure(num=1, clear=True)
mann_plot.set_size_inches(6, 6)
num1 = mann_plot.add_subplot(1, 1, 1, projection='3d')
final = num1.plot_surface(bx, hx, ux, cmap=cm.terrain)
num1.set(xlabel='Width B, m',
       ylabel = 'Depth H, m',
       zlabel = 'Veloctiy U, m/s',
       xticks = [0,5,10,15,20],
       yticks = [0,1,2,3,4,5],
       zticks = [0, .5, 1, 1.5, 2, 2.5, 3, 3.5],
       title = 'Velocity Using Manning’s Equation')
mann_plot.colorbar(final)

num1.view_init(elev = 35, azim = -135)

mann_plot.savefig('water_channel.png')
       

