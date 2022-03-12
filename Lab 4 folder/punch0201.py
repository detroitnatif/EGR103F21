#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:34:09 2021

@author: tylerklimas
"""

def factor_count(n,f):
    count = 0
    for num in range (10**(n-1), 10**(n)):
        if num % f == 0:
            count += 1
    return count


if __name__ == '__main__':
    print(factor_count(2,8))

        
        
        
        
    