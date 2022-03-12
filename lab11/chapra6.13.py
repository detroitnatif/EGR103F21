#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:25:28 2021

@author: tylerklimas
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
    
