#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 20:52:31 2021

@author: tylerklimas
"""

def digit_sum(n):
    if n == 0:
        return 0
    val = int(n%10) + digit_sum(int(n//10))
    final = (val%10) + digit_sum(val//10)
    
    return final 
    