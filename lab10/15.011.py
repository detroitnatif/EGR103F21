#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:20:01 2021

@author: tylerklimas
[15.011.py]
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


i = np.array([50, 80, 130, 200, 250, 350, 450, 550, 700])
p = np.array([99, 177, 202, 248, 229, 219, 173, 142, 72])

def fun(x, *coefs):
    return coefs[0] * (x/coefs[1])*np.exp(-1*x/coefs[1] + 1)

popt = opt.curve_fit(fun, i, p, [200, 200])[0]
print(popt)

phat = fun(i, *popt)
imodel = np.linspace(i.min(), i.max(), 100)
pmodel = fun(imodel, *popt)



def make_plot(x, y, yhat, xmodel, ymodel, fig_num=1):
    fig, ax = plt.subplots(num=fig_num, clear=True)
    ax.plot(x, y, "rd", label="Data")
    #ax.plot(x, yhat, "ks", label="Estimates", mfc="none")
    ax.plot(xmodel, ymodel, "g-", label="Model")
    ax.grid(True)
    ax.legend(loc="best")
    ax.set_ylabel('Photosynthesis Rate (mg $m^-3 d^-1$)')
    ax.set_xlabel('Solar Radiation (\u03BCE $m^-2 s^-1$)')
    fig.tight_layout()
    fig.savefig('15.011.png')
    return fig, ax

make_plot(i, p, phat, imodel, pmodel)

calc_stats(p, phat)

