#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:51:28 2021

@author: tylerklimas
"""

def bit(bit):
    num = 1
    d = (str(bit)[::-1])
    for idx, ele in enumerate(d):
        if ele == '1':
            num = num + (int(idx)**2)-2
    return num