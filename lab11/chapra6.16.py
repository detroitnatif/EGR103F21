#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tylerklimas
[chapra6.16.py]
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

r = 7
l = 5


def fun(r, h):
    l = 5
    v = ((((r**2) * (np.arccos((r-h)/r))) - ((r-h)*np.sqrt((2*r*h) - h**2)))*l) - 8 
    return v


r = opt.brentq(lambda h: fun(7, h), 0, 1)
print(r)
    
