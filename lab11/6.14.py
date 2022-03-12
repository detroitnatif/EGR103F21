#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tylerklimas
[6.14.py]
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


def fun(x, pt):
    k = (x/(1-x))*(np.sqrt((2*pt)/(2+x)))
    return k 


x1 = np.linspace(0, .05, 100)
k = fun(x1, 3)

graph = plt.figure(num = 1, clear = True)
graph.set_size_inches(4, 3, forward=True)
ax = graph.add_subplot(1,1,1)
ax.plot(x1, k)
ax.set_xlabel('x (Mole fraction of $H_2O$)')
ax.set_ylabel('Equillbrium Constant (K)')
graph.tight_layout()
ax.grid(True)
ax.set_title("Graph of Equillbrium Constant vs. Mole fraction of $H_2O$")
graph.savefig('chapra_6_014_plot.png')



r1 = opt.brentq(lambda x: fun(x, 3)-.05, .02, .05)
print(r1)

