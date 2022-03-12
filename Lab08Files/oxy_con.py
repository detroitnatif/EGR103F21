#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:14:28 2021

@author: tylerklimas
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as axes3d
from matplotlib import cm

load = np.loadtxt('chapra_p15_5.dat')
matrix = np.matrix(load)


col1 = matrix[:, [0]]
col2 = matrix[:, [1]]
col3 = matrix[:, [2]]


c = col1.reshape(7,3)
t = col2.reshape(7,3)
oc = col3.reshape(7,3)

oxy = plt.figure(num=1, clear=True)
triplot = oxy.add_subplot(1, 1, 1, projection='3d')

dplot = triplot.plot_surface(c, t, oc, cmap=cm.plasma)

oxy.tight_layout()

triplot.set(xlabel='c, g/L', 
       ylabel='T, C', 
       zlabel='OC, mg/L',
       xticks = [0, 5, 10, 15, 20, 25, 30],
       yticks = [0, 5, 10, 15, 20, 25, 30],)

triplot.view_init(elev=31, azim=35)
