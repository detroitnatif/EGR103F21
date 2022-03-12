#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:09:14 2021

@author: tylerklimas
[chapra_genfit.py]
[Tyler Klimas]
[11-13-21]

Using Egr93's "Lab 9 common code"

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,2,4,6,9,11,12,15,17,19])
y = np.array([5,6,7,6,9,8,8,10,12,12])

xv = np.reshape(x, (-1,1))
yv = np.reshape(y, (-1, 1))
p = np.block([xv**1, xv**0])
q = np.block([yv**1, yv**0])

pvec = np.linalg.lstsq(p, y, rcond=1)[0]
qvec = np.linalg.lstsq(q, x, rcond=1)[0]
print('{:.3e}'.format(pvec[0]))
print('{:.3e}'.format(pvec[1]))
print('{:.3e}'.format(qvec[0]))
print('{:.3e}'.format(qvec[1]))


def yfun(xe, coefs):
    return coefs[0] * xe**1 + coefs[1] * xe**0

yhat = yfun(x, pvec)
xhat = yfun(y, qvec)

def calc_stats(y, yhat, to_print=1):
    # Calculate statistics
     st = np.sum((y - np.mean(y)) ** 2)
     sr = np.sum((y - yhat) ** 2)
     r2 = (st - sr) / st
     if to_print:
         print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
     return st, sr, r2

st, sr, r2 = calc_stats(y, yhat, 1)
stx, srx, r2x = calc_stats(x, xhat, 1)
r = (r2)**(1/2)
print('{:.3e}'.format(r))
rx = (r2x)**(1/2)
print('{:.3e}'.format(rx))
sy_x = (sr/(len(x)-2))**(1/2)
print('{:.3e}'.format(sy_x))
sx_y = (srx/(len(y)-2))**(1/2)
print('{:.3e}'.format(sx_y))


pic = plt.figure(num=1, clear=True)
graph = pic.subplots(2,1)
pic.set_size_inches(6,4,forward=True)


xmod=np.linspace(x.min(), x.max(), 100)
line1 = np.polyval(pvec, xmod)
pre1 =np.polyval(pvec,x)


ymod = np.linspace(x.min(), x.max(), 100)
line2 = np.polyval(qvec, ymod) 
pre2 = np.polyval(qvec, y)


graph[0].plot(x,y, 'yo', label='data')

graph[0].plot(xmod, line1, 'c', label='model')

graph[0].plot(x, pre1, 's', label='estimate')

graph[0].set(xlabel='X', ylabel='Y')
graph[0].grid(True)


graph[1].plot(y,x, 'ko', label='data')

graph[1].plot(ymod, line2, label='model')

graph[1].plot(y, pre2, 's', label='estimate')

graph[1].set(xlabel='X',
          ylabel='Y')
graph[1].grid(True)

plt.legend(labels=['data', 'model', 'estimate'], loc='best')

pic.tight_layout()
pic.savefig('c1.png')
































