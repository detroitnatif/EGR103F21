#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:09:14 2021

@author: tylerklimas
[chapra15_006.py]
[Tyler Klimas]
[11-13-21]

Using Egr93's "Lab 9 common code"

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm


def calc_stats(y, yhat, to_print=True):
    # Calculate statistics
    st = np.sum((y - np.mean(y)) ** 2)
    sr = np.sum((y - yhat) ** 2)
    se = np.sqrt(sr/(len(y) -2))
    r2 = (st - sr) / st
    r = np.sqrt(r2)
    if to_print:
        print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
    return st, sr, se, r2, r


def make_plot(x, y, yhat, xmodel, ymodel, fig_num=1):
    fig, ax = plt.subplots(num=fig_num, clear=True)
    ax.plot(x, y, "ko", label="Data")
    ax.plot(x, yhat, "ks", label="Estimates", mfc="none")
    ax.plot(xmodel, ymodel, "k-", label="Model")
    ax.grid(True)
    ax.legend(loc="best")
    fig.tight_layout()
    return fig, ax

load = np.loadtxt('chapra_p15_5.dat')
xm = np.reshape(load[:, 1].copy(), (7, 3))
ym = np.reshape(load[:, 0].copy(), (7, 3))
zm = np.reshape(load[:, 2].copy(), (7, 3))
xmodelm, ymodelm = np.meshgrid(np.linspace(xm.min(), xm.max(), 19), np.linspace(ym.min(), ym.max(), 7))


xv = np.reshape(xm, (-1, 1))
yv = np.reshape(ym, (-1, 1))
zv = np.reshape(zm, (-1, 1))
phi = np.block([[xv**0, xv**1, yv**1]])
pvec = np.linalg.lstsq(phi, zv, rcond=None)[0]

def zfun(xe, ye, coefs):
    return coefs[0] * xe**0 + coefs[1] * xe**1 + coefs[2] * ye**1

a = zfun(12, 15, pvec)
b = abs((a-9.09))/ 9.09 * 100

zhatv = zfun(xv, yv, pvec)
zhatm = zfun(xm, ym, pvec)
zmodelm = zfun(xmodelm, ymodelm, pvec)

calc_stats(zv, zhatv, 1)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface(xmodelm, ymodelm, zmodelm, cmap = 'winter')
ax.set(xlabel = 't')
ax.view_init(20, -5)
fig.savefig('15_006.png')



fig = plt.figure(num=2, clear=True)
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface(xm, ym, zm-zhatm, cmap = cm.autumn)
ax.set(xlabel = 't')
fig.set_size_inches(6, 4, forward=True)
fig.tight_layout()
fig.savefig('chapra_15_006_plot2.png')
































