#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:37:23 2021

@author: tylerklimas
"""
a = []
def first_last6(a):
    if a[0] == 6:
        return True
    if a[len(a)-1] == 6:
        return True
    else:
        return False
print(first_last6([1, 2, 3, 5, 6]))
    