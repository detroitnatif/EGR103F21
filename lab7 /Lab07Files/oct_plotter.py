#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:53:52 2021

@author: tylerklimas
[oct_plotter.py]
[Tyler Klimas]
[10-21-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import matplotlib.pyplot as plt
from chapra_08_16 import rotate_2d

x = np.array([2, 1, 1, 2, 3, 4, 4, 3, 2])
y = np.array([1, 2, 3, 4, 4, 3, 2, 1, 1])
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)

for k in np.arange(0, 360, 30):
    x2, y2 = rotate_2d(k, x, y)
    ax.plot(x2, y2,
            color=[(1+np.cos(2*np.pi*k/720))/2,
                   (1+np.cos(2*np.pi*(k+120)/720))/2,
                   (1+np.cos(2*np.pi*(k+240)/720))/2])
ax.axis('equal')
fig.tight_layout()
fig.savefig('oct.png')