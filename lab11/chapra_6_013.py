#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tylerklimas
[chapra_6_013.py]
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

def fun(x):
    return (.99403 + (1.671*(10**(-4))*x) + (9.7215 *(10**(-8))*(x**2)) -
            (9.5838*(10**(-11)*(x**3))) + (1.9520 * (10**(-14)) * (x**4))) - 1.1 

t = np.linspace(-1200, 1200, 100)
tv = fun(t)

fig = plt.figure(num = 1, clear = True)
ax = fig.add_subplot(1,1, 1)
ax.plot(t, tv, 'r-')
ax.set_xlabel('Tempature (K)')
ax.set_ylabel('Specific Heat ($c_p$)')
ax.set_title('Tempature vs Specific Heat')
fig.tight_layout()
fig.savefig('chapra_6_013_plot.png')

r1 = opt.brentq(lambda x: fun(x),-600, 2000)
print(r1)
            