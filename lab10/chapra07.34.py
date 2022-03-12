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



def fun(s):
    t = -1*((15*s)*(1-s))/((1-s)*(4*s**2-3*s+4))
    return t


out1 = opt.fminbound(fun, 0, 5)
out2 = opt.fmin(fun, 2)[0]

print(out1, out2)

print(fun(out1), fun(out2))