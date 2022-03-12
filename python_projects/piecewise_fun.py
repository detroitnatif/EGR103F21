#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:57:17 2021

@author: tylerklimas
"""

import numpy as np
import matplotlib.pyplot as plt

def fun(t):
    out = ((t<=0) * (0) +
           ((0<t) & (t<=1)) * (t) +
           ((1<t) & (t<=3)) * (1) +
           ((3<t) & (t<=4)) * (-t + 4) +
           (t>4) * (0))
    return out

t = np.linspace(-1, 5, 100)
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1)
ax.plot(t, fun(t))
