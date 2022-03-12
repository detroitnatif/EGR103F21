#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 18:17:44 2021

@author: tylerklimas

[gettin_sleepy.py]
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

z = np.arange(0, 6*np.pi + 6*np.pi/64, np.pi/64)

x1 = z*np.cos(6*z)
y1 = z*np.sin(6*z)
z1 = z

helix = plt.figure(num=1, clear=True)
top = helix.add_subplot(2, 1, 1)
top.plot(x1, y1, 'r')
top.set(xlabel='x',
       ylabel='y')

bottom = helix.add_subplot(2, 1, 2,  projection='3d')
bottom.plot(x1, y1, z1, 'c')
bottom.set(xlabel='x',
        ylabel='y',
        zlabel='z',
        xticks=[-20, 0, 20],
        yticks=[-20, 0, 20],
        zticks=[0,10,20],
        zlim = [0,20])
helix.set_size_inches(6,8)
helix.tight_layout()
top.grid(True)
top.axis('equal')

helix.savefig('helix.png')