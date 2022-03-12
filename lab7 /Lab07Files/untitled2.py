#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:47:58 2021

@author: tylerklimas
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