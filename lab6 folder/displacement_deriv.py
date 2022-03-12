#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:27:39 2021

@author: tylerklimas
[displacement_deriv.py]
[Tyler Klimas]
[10-16-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import matplotlib.pyplot as plt

def displacement(x, l, e, i, w):
    y = (w/(120*e*i*l))*(-x**5+(2*(l**2)*(x**3))-(l**4)*x)
    return y

def slope(x, l, e, i, w):
    theta = (w/(120*e*i*l))*(-5*(x**4)+(6*(l**2)*(x**2))-(l**4))
    return theta

def moment(x, l, e, i, w):
     m = (w/(120*l))*(-20*(x**3)+(12*x*(l**2)))
     return m 

def shear(x, l, e, i, w):
    v = (w/(120*l))*(-60*(x**2)+12*(l**2))
    return v

def loading(x, l, e, i, w):
     wx = (w/(120*l))*(120*x)
     return wx
    
x = np.linspace(0, 600, 101)
l = 600 
e = 50000
i = 30000
w = 2.5


y_1 = displacement(x, l, e, i, w)
theta_1 = slope(x, l, e, i, w)
m_1 = moment(x, l, e, i, w)
v_1 = shear(x, l, e, i, w)
wx_1 = loading(x, l, e, i, w)


fig = plt.figure(num = 1, clear=True)
fig.set_size_inches(6, 8, forward=True)


ax = fig.subplots(5,1, sharex=True)
ax[0].plot(x, y_1, 'r^-', markevery=10)
ax[0].set_ylabel('cms')

ax[1].plot(x, theta_1, 'ys-', markevery=10)
ax[1].set_ylabel('cm/cm')


ax[2].plot(x, m_1, 'bp-', markevery=10)
ax[2].set_ylabel('kN-cm')


ax[3].plot(x, v_1, 'ch-', markevery=10)
ax[3].set_ylabel('kN')


ax[4].plot(x, wx_1, 'kx-', markevery=10)
ax[4].set_ylabel('kN/cm')
ax[4].set_xlabel('cms')


fig.tight_layout()
fig.savefig('disp_deriv.png')

