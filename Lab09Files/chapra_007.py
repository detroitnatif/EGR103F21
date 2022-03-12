#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:09:14 2021

@author: tylerklimas
[chapra_007.py]
[Tyler Klimas]
[11-13-21]

Using Egr93's "Lab 9 common code"

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

con = np.array([[0,10,20],
              [0,10,20],
               [0,10,20],
               [0,10,20],
               [0,10,20],
               [0,10,20],
               [0,10,20]])

Temp = np.array([[0,0,0],
                [5,5,5],
                [10,10,10],
                [15,15,15],
                [20,20,20],
                [25,25,25],
                [30,30,30]])

oc_1 = np.array([[14.6,12.9,11.4],
                  [12.8,11.3,10.3],
                  [11.3,10.1,8.96],
                  [10.1,9.03,8.08],
                  [9.09,8.17,7.35],
                  [8.26,7.46,6.73],
                  [7.56,6.85,6.20]])

def calc_stats(y, yhat, to_print=True):
    # Calculate statistics
    st = np.sum((y - np.mean(y)) ** 2)
    sr = np.sum((y - yhat) ** 2)
    r2 = (st - sr) / st
    if to_print:
        print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
    return st, sr, r2


def make_plot(x, y, yhat, xmodel, ymodel, fig_num=1):
    fig, ax = plt.subplots(num=fig_num, clear=True)
    ax.plot(x, y, "ko", label="Data")
    ax.plot(x, yhat, "ks", label="Estimates", mfc="none")
    ax.plot(xmodel, ymodel, "k-", label="Model")
    ax.grid(True)
    ax.legend(loc="best")
    fig.tight_layout()
    return fig, ax

def zfun(xe,ye,coefs):
    return coefs[0]* ye ** 0 * xe ** 0 + coefs[1]* xe + coefs[2]* ye ** 3 + coefs[3]* ye ** 2 + coefs[4]*ye ** 1





xcolumn = np.reshape(Temp,(-1,1))
ycolumn = np.reshape(con ,(-1,1))
zcolumn = np.reshape(oc_1 ,(-1,1))
pmat = np.block([[(xcolumn * ycolumn)** 0,ycolumn,xcolumn ** 3,xcolumn ** 2,xcolumn ** 1]])


pvec = np.linalg.lstsq(pmat,zcolumn,rcond = None)[0]


print(pvec)

zhatc = zfun(xcolumn,ycolumn,pvec)

zhatm = zfun(con,Temp,pvec)

zhatc = np.reshape(zhatc ,(7,3))

calc_stats(oc_1,zhatc,1)

[cv,tv]= np.meshgrid(np.linspace(0,20,7),np.linspace(0,30,19))

m1 = zfun(tv,cv,pvec)

fig = plt.figure(num = 1,clear = True)

ax =fig.add_subplot(1,1,1,projection ='3d')

ax.plot_surface(tv,cv,m1,cmap ='YlOrRd')

ax.set(xlabel ='T,$ˆ{\ c i r c}$C',ylabel ='c,g/L',zlabel ='OC,mg/L')

ax.set(xticks = np.linspace(0,30,7),yticks = np.linspace(0,20,3))


ax.view_init(azim = 10,elev = 17.5)

fig.set_size_inches(6,4,forward = True)

fig.tight_layout()

fig.savefig('chapra.007_1.png')

residual = oc_1 - zhatm

fig2 = plt.figure(num = 2,clear = True)

ax2 =fig2.add_subplot(1,1,1,projection ='3d')

ax2.plot_surface(Temp,con,residual,cmap ='seismic')

ax2.set(xlabel ='T,$ˆ{\ c i r c}$C',ylabel ='c,g/L',zlabel ='Residual,mg/L')

ax2.view_init(azim = -40,elev = 37.5)

fig2.set_size_inches(6,4,forward = True)

fig2.tight_layout()

fig2.savefig('chapra.007_2.png')
