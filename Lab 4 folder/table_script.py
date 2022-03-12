#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:01:11 2021

@author: tylerklimas
"""
import numpy as np

r = 12
c = 12
def mult_table(r, c):
    table = ' '
    for col in range(c):
        table += '{:5}'.format(col+1)
    for row in range(r):
        table += '\n' + '{:2}'.format(row+1)
        for column in range(c):
            table += '{:4}'.format((row+1) * (column+1))
    table = table + '\n' 
    return table

print(mult_table(3,3))
    



    
    