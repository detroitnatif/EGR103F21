#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:09:14 2021

@author: tylerklimas
[15.10_alt.py]
[Tyler Klimas]
[11-13-21]

Using Egr93's "Lab 9 common code"

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import matplotlib.pyplot as plt

def calc_stats(y, yhat, to_print=True):
    # Calculate statistics
    st = np.sum((y - np.mean(y)) ** 2)
    sr = np.sum((y - yhat) ** 2)
    r2 = (st - sr) / st
    if to_print:
        print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
    return st, sr, r2

def yfun(xe, coefs):
    return (coefs[0]*np.exp(-1.5*xe) + coefs[1]*np.exp(-.3*xe) +
            coefs[2]*np.exp(-.2*xe))

t = np.array([0.5, 1, 2, 3, 4, 5, 6, 7, 9])
pt = np.array([6, 4.4, 3.2, 2.7, 2, 1.9, 1.7, 1.4, 1.1])

tv = np.reshape(t, (-1,1))
ptv = np.reshape(pt, (-1, 1))
phi_mat = np.block([[np.exp(-1.5*tv), np.exp(-.3*tv), np.exp(-.2*tv)]])
pvec = np.linalg.lstsq(phi_mat, pt, rcond=None)[0]

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1)
fig.set_size_inches(6,4,forward=True)
xmod = np.linspace(t.min(), t.max(), 100)
line = yfun(xmod, pvec)
ax.plot(xmod, line, 'k-')
ax.grid(True)
g1 = pvec[0]*np.exp(-1.5*xmod)
g2 = pvec[1]*np.exp(-.3*xmod)
g3 = pvec[2]*np.exp(-.05*xmod)
ax.plot(xmod, g1, 'b.', markevery=2)
ax.plot(xmod, g2, 'g--',  markevery=10)
ax.plot(xmod, g3, 'r.--',  markevery=10)
ax.plot(t, pt, 'mo')
linedata = yfun(t, pvec)
ans = calc_stats(pt, linedata)

fig.savefig('15.10alt.png')