#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:53:52 2021

@author: tylerklimas
[connect_code7.py]
[Tyler Klimas]
[10-21-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""
import numpy as np

def rotate_2d(n, xv, yv):
    xv1= np.array(xv)
    yv1 = np.array(yv)
    ang = np.radians(n)
    q = np.block([[yv1], [xv1]])
    m = np.array([[np.cos(ang), -1*np.sin(ang)], [np.sin(ang), np.cos(ang)]])
    rotate = m @ q
    first_row = rotate[0]
    sec_row = rotate[1]
    return first_row , sec_row
