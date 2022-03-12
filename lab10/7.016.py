#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:08:01 2021


@author: tylerklimas
[7.016.py]
[Tyler Klimas]
[11-20-21]

Using Egr93's "Lab 9 common code"

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import scipy.optimize as opt
from lab10_common import *

q = 75
rw = 6/1000
k = .17
h = 12
ta = 293
t = np.linspace(0, .05, 1000)

def fun(t):
    return (ta + (q/(2*np.pi))*((1/k)*np.log((rw + t)/rw) + (1/h)*(1/(rw + t))))

out1 = opt.fminbound(fun, .003, .2)
out2 = opt.fmin(fun, 0)
print(out1*1000)
print(out2*1000)

temp = fun(t)
temp1 = fun(out1)
temp2 = fun(out2)
print(temp1, temp2)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.plot(t, temp, 'c')
ax.set_xlabel('Insulation Thickness (m)')
ax.set_ylabel('Tempature (K)')
ax.set_title('Insulation Thickness (m) vs Tempature (K)')
fig.savefig('chapra_07_016.png')
tan = np.linspace(.005, .015, 100)
tanl = 
ax.plot(tan, temp1, 'k')

