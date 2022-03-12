#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 11:49:15 2021

@author: tylerklimas
[15.029.py]
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
import matplotlib.pyplot as plt

t = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130])
rpa = np.array([82, 2300, 18500, 80500, 2.3*10**5, 5*10**5,
               9.6*10**5, 1.5*10**6, 2.4*10**6])
pa = np.log(np.array([82, 2300, 18500, 80500, 2.3*10**5, 5*10**5,
               9.6*10**5, 1.5*10**6, 2.4*10**6]))

def fun(t, *coef):
    return coef[0] - (coef[1]/(coef[2] + t))

popt = opt.curve_fit(fun, t, pa, [70, 18500, 10])[0]
print(popt)

yhat = fun(t, *popt)
xhat = fun(pa, *popt)
xmod = np.linspace(50, 130, 100)
ymod = fun(xmod, *popt)

st, sr, r2 = calc_stats(pa, yhat, 1)

sp_t = (sr/(len(t)-3))**(1/2)
print('{:.3e}'.format(sp_t))

graph = plt.figure(num=1, clear =True)
p = graph.add_subplot(1,1,1)
p.plot(t, pa, 'ch')
p.plot(xmod, ymod, 'k--')
p.set_xlabel('Tempature (K)')
p.set_ylabel('Vapor Pressure (pa)')
p.set_title('Antoine Equation')
p.grid(True)
graph.tight_layout()
graph.savefig('chapra_15_029.png')


