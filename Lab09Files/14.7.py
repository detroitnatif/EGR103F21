#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:09:14 2021

@author: tylerklimas
[14.7.py]
[Tyler Klimas]
[11-13-21]

Using Egr93's "Lab 9 common code"

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""
import numpy as np

v = 10
q = 1000
nm = 28
n = q/nm
t = np.array([-40, 0, 40, 80, 120, 160])+273.15
p = np.array([6900, 8100, 9350, 10500, 11700, 12800])
def stoich(p, v, n, t):
    r = (p*v)/(n*t)
    return r 
w = np.mean(stoich(p, v, n, t))




def zfun(xe, coefs):
    return coefs[0] * xe**1 
    
xv = np.reshape(t, (-1, 1))
 
yv = np.reshape(p, (-1, 1))

phi_mat = np.block([[xv**1]])

pvec = np.linalg.lstsq(phi_mat, yv, rcond=None)[0]

q = t*pvec[0][0]
yhat = zfun(t, pvec)
print(yhat)


def calc_stats(y, yhat, to_print=True):
    # Calculate statistics
    st = np.sum((y - np.mean(y)) ** 2)
    sr = np.sum((y - yhat) ** 2)
    r2 = (st - sr) / st
    if to_print:
        print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
    return st, sr, r2

a = calc_stats(p, yhat)




    