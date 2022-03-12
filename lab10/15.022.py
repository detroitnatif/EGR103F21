#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 11:23:56 2021

@author: tylerklimas
[15.022.py]
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

x1 = np.array([.5, 1, 2, 3, 4])
y1 = np.array([10.4, 5.8, 3.3, 2.4, 2])

def fun(x, *coefs):
    return ((coefs[0] + np.sqrt(x))/(coefs[1]*np.sqrt(x)))**2

popt = opt.curve_fit(fun, x1, y1, [2, 2])[0]
print(popt[0], popt[1])

ans = fun(1.6, *popt)
print(ans)
xmodel = np.linspace(x1.min(), x1.max(), 100)
ymodel = fun(xmodel, *popt)
yhat = fun(x1, *popt)

def make_plot(x, y, yhat, xmodel, ymodel, fig_num=1):
    fig, ax = plt.subplots(num=fig_num, clear=True)
    ax.plot(x, y, "ms", label="Data")
    #ax.plot(x, yhat, "ks", label="Estimates", mfc="none")
    ax.plot(xmodel, ymodel, "y-", label="Model")
    ax.grid(True)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig('15.022.png')
    return fig, ax

make_plot(x1, y1, yhat, xmodel, ymodel)

calc_stats(y1, yhat)

