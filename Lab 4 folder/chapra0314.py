#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import math as m 
import matplotlib.pyplot as plt

def rocket(t):
    out = (((0<=t) &  (t<= 8)) * (10*t**2 - 5*t) +
           ((8 < t) & (t <= 16)) * (-3*t + 624) +
           ((t > 16 ) & ( t <= 26)) * (36*t + 12*(t-16)**2) +
           ((t>26) * (2136*(m.e**(((-1)*.1)*(t-26))))))
    return out

t = np.linspace(0, 50, 100)
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1)
ax.plot(t, rocket(t))
