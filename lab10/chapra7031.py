#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:20:01 2021

@author: tylerklimas
[chapra7031.py]
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

os = 10
kd = .1
ka = .6
ks = .05
lo = 30
sb = 1

def fun(t):
    return (os - ((kd*lo)/(kd+ks-ka))*((np.exp(-ka*t)) -
                                        np.exp(-1*(kd+ks)*t))
                  - ((sb/ka)*(1-np.exp(-ka*t))))

out1 = opt.fminbound(fun, 2, 5)
out2 = opt.fmin(fun, 2)[0]
print(out1, out2)

con1 = fun(out1)
con2 = fun(out2)
print(con1, con2)

t = np.linspace(0, 20, 100)
tv = fun(t)
fig =plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1)
ax.plot(t, tv, 'r-')
ax.set_xlabel('t (d)')
ax.set_ylabel('o mg/L')
ax.set_title('Streeter-Phelps model')
fig.tight_layout()
fig.savefig('chapra_7_031_plot.png')

