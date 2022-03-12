#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:52:11 2021

@author: tylerklimas
"""
import numpy as np
f = np.array([14, 18, 8, 9, 13])
x = np.array([.013, .020, .009, .010, .012])
def kv(fr, xv):
    k = fr/xv
    return k
def uv(kv, xv):
    u = (1/2)*(kv)*((xv)**(2))
    return u

a = kv(f, x)

b = uv(a, x)

answer = round(np.max(b), 2)
print(answer)

    

