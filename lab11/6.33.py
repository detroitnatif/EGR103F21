#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tylerklimas
[6.33.py]
[Tyler Klimas]
[11-20-21]

Using Egr93's "Lab 9 common code"

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def fun(t):
    c = 15 - (77*np.exp(-1.5*t) + 20*np.exp(-.08*t))
    return c


t1 = np.linspace(0, 10, 100)
y1 = fun(t1)

graph = plt.figure(num = 1, clear = True)
ax = graph.add_subplot(1,1,1)
ax.plot(t1, y1)
ax.set_xlabel('x')
ax.set_ylabel('y')
graph.tight_layout()
ax.grid(True)


r = opt.fsolve(fun, 5)
print(r)