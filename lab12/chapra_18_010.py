#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tylerklimas
[chapra_18_010.py]
[Tyler Klimas]
[11-29-21]


I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.interpolate import interp1d 
import matplotlib.pyplot as plt

x = np.array([0,2,4,7,10,12])
y = np.array([20,20,12,7,6,6])

cub = CubicSpline(x, y)
clamp = CubicSpline(x, y, bc_type = 'clamped')

xmod = np.linspace(x.min(), x.max(), 100)

y1 = cub(1.5)
y2 = clamp(1.5)
print(y1, y2)

fig = plt.figure(num=1, clear=True)
ax =fig.add_subplot(1,1,1)

ax.plot(x, y, 'mo')
ax.plot(xmod, cub(xmod), 'r')
ax.plot(xmod, clamp(xmod), 'b--')

plt.legend(['Data', 'Cubic Spline', 'Clamped'], loc='best')

fig.savefig('chapra_18_010_plot.png')