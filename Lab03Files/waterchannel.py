#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:26:49 2021

@author: tylerklimas
"""
import numpy as np
s = np.array([.0001, .0002, .0010, .0007, .0003])
n = np.array([.035, .020, .015, .030, .022])
b = np.array([10, 8, 20, 24, 15])
h = np.array([2, 1, 1.5, 3, 2.5])

def channel(n, s, b, h):
    u = ((s**(1/2)/n)*(((((b*h)/(b+(2*h))))**2)**1/3))
    return u
         


answer = channel(n, s, b, h)
print(answer)



