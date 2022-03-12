#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 19:27:56 2021

@author: tylerklimas
"""

import numpy as np
import scipy.optimize as opt


def fun(x):
    return -1*((.7/(np.sqrt(1+x**2)))-(np.sqrt(1+x**2))*(1-(.7/(1+x**2)))+x)

out1 = opt.fminbound(lambda x: fun(x), 0, 4)
out2 = opt.fmin(fun, 4)[0]

print(out1, out2)

print(fun(out1), fun(out2))