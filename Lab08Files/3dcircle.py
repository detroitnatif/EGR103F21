#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 11:52:04 2021

@author: tylerklimas

[3dcircle.py]
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

phi, theta = np.meshgrid(np.arange(0, np.pi + np.pi/20, np.pi/20),
np.arange(0, 2*np.pi+ np.pi/40, np.pi/40))

x_coor = np.sin(phi)*np.cos(theta)
y_coor = np.sin(phi)*np.sin(theta)
z_coor = np.cos(phi)

sphere = plt.figure(num=1, clear=True)
splot = sphere.add_subplot(1, 1, 1, projection='3d')

num1 = splot.plot_wireframe(x_coor, y_coor, z_coor, color = 'g')


sphere.set_size_inches(6, 6, forward=True)
sphere.tight_layout()
splot.set(xlabel='x', 
       ylabel='y', 
       zlabel='z',
       xticks = [-1, 0, 1],
       yticks = [-1, 0, 1],
       zticks = [-1, 0, 1],)

splot.view_init(elev=8, azim=340)


sphere.savefig('sphere.png')