#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:09:14 2021

@author: tylerklimas
[14.27.py]
[Tyler Klimas]
[11-13-21]

Using Egr93's "Lab 9 common code"

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""
import numpy as np
import matplotlib.pyplot as plt

v = np.array([2, 3, 4, 5, 7, 10])
i = np.array([5.2, 7.8, 10.7, 13, 19.3, 27.5])

xv = np.reshape(v, (-1,1))
iy = np.reshape(i, (-1, 1))
p = np.block([xv**1, xv**0])
q = np.block([xv**1])
gen_fit = np.linalg.lstsq(p, iy, rcond=None)[0]

gen_fit2 = np.linalg.lstsq(q, iy, rcond=None)[0]



graph = plt.figure(num=1, clear=True)
p1 = graph.add_subplot(1,1,1)
graph.set_size_inches(6,4,forward=True)
vmod=np.linspace(v.min(), v.max(), 100)


line = np.polyval(np.polyfit(v, i, 1), vmod)
p1.plot(vmod, line, 'b')



def zfun(xe, coefs):
    return coefs[0]*xe**1

def xfun(xe, coefs):
    return coefs[0]*xe**1 + coefs[1]*xe**0


line1 = zfun(vmod, gen_fit)
p1.plot(vmod, line1, 'r--')
p1.set(xlabel='V',
       ylabel='i')
plt.legend(labels=['data', 'model', 'zero intercept model'], loc='best')
p1.grid(True)
p1.plot(v, i, 'ko')

def calc_stats(y, yhat, to_print=1):
    # Calculate statistics
     st = np.sum((y - np.mean(y)) ** 2)
     sr = np.sum((y - yhat) ** 2)
     r2 = (st - sr) / st
     if to_print:
         print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
     return st, sr, r2
 
yhat = xfun(v, gen_fit)
a = calc_stats(i, yhat)


yhat2 = zfun(v, gen_fit2)

b = calc_stats(i, yhat2)

graph.tight_layout()
graph.savefig('14.27.png')







