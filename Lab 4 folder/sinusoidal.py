#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[sinusoidal.py]
[Tyler Klimas]
[9-19-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import matplotlib.pyplot as plt
def y(t, A, omega, phi):
    val = A*np.cos(omega*t + phi)
    return val
t = np.linspace(-2*np.pi, 2*np.pi, 101)
x1 = y(t, 1, 1, 0)
x2 = y(t, 2, 1, 0)
x3 = y(t, 1, 2, 0)
x4 = y(t, 1, 1, np.pi/4)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)

ax.plot(t, x1, 'b^-', markevery=10, mec='r', mfc='m', label= '$y(t, 1, 1, 0)$')
ax.plot(t, x2, 'ys--', markeredgecolor='r', markerfacecolor='m', markevery=10, label= '$y(t, 2, 1, 0)$')
ax.plot(t, x3, 'bp:', mec='c', mfc='m', markevery=10, label = '$y(t, 1, 2, 0)$')
ax.plot(t, x4, 'bh-.', mec='r', mfc='g', markevery=10, label = '$y(t, 1, 1, \pi/4)$')
plt.legend(loc='best')
plt.show
fig.tight_layout()
fig.savefig('cosine_plot.png')    
    