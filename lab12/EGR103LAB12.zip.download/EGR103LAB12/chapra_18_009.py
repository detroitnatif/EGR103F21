#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tylerklimas
[chapra_18_009.py]
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


t = np.array([0,8,16,24,32,40])
o = np.array([14.621, 11.843, 9.870, 8.418, 7.305, 6.413])

lin = interp1d(t, o, kind='linear')
poly = interp1d(t, o, kind=5)
cub = CubicSpline(t, o)

o27 = lin(27)
o275 = poly(27)
o27s = cub(27)
print(o27, o275, o27s)
x = np.linspace(t.min(), t.max(), 100)

fig = plt.figure(num=1, clear=True)
ax =fig.add_subplot(1,1,1)
ax.plot(t, o, 'mo')
ax.plot(x, lin(x), 'r', label='Linear')
ax.plot(x, poly(x), 'g--', label = 'Polynomial')
ax.plot(x, cub(x), 'b--', label= 'Cubic Spline')
plt.legend(loc='best')

fig.savefig('chapra_18_009.png')
