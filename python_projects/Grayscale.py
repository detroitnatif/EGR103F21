#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:11:28 2021

@author: tylerklimas
"""

def convert(r, g, b):
    col = .21*r + .71*g + .07*b
    return col 

x=convert(0,0,0)
print(x)