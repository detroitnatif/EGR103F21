#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 19:12:52 2021

@author: tylerklimas
"""
import numpy as np
m = np.array([83.6 , 60.2 , 72.1 , 91.1 , 92.9 , 65.3 , 80.9])
vt = np.array([53.4 , 48.5 , 50.9 , 55.7 , 54 , 47.7 , 51.1])
A = np.array([0.455 , 0.402 , 0.452 , 0.486 , 0.531 , 0.475 , 0.487])
p = 1.793
g = 9.81
def drag():
    cd = g*m/(vt**2)
    return cd
cd = drag()
cdavg = np.mean(drag())
cdmin = np.round((np.min(drag())), 4)
cdmax = np.round((np.max(drag())), 4)
def vpred():
    va = (g*m/cdavg)**(1/2)
    return va
va = vpred()
def work():
    cdi = m*g/(va**2)
    return cdi
cdi = work()
def coef():
    CD = 2*cd/(p*A)
    return CD
print(coef())
CDavg = np.mean(coef())
CDmax = np.max(coef())
