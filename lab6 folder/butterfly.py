#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:53:52 2021

@author: tylerklimas
[butterfly.py]
[Tyler Klimas]
[10-17-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import math as m 
import matplotlib.pyplot as plt

def butterfly(t):
    x = np.sin(t)*((np.e**(np.cos(t)))-(2*np.cos(4*(t))-(np.sin(t/12)**5)))
    y = np.cos(t)*((np.e**(np.cos(t)))-(2*np.cos(4*(t))-(np.sin(t/12)**5)))
    return x, y
z = np.arange(0, 100+1/16, 1/16)
x_1, y_1 = butterfly(z)

fig = plt.figure(num = 1, clear=True)
fig.set_size_inches(6, 8, forward=True)

ax = fig.subplots(2,2)
ax[0][0].plot(z, x_1, 'r-', markevery=1/16)
ax[0][1].plot(x_1, y_1, 'y-', markevery=1/16)
ax[1][1].plot(x_1, z, 'b-', markevery=1/16)
fig.delaxes(ax[1][0])
fig.tight_layout()
fig.savefig('butterfly.png')
