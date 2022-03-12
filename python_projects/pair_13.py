#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:23:41 2021

@author: tylerklimas
"""

def pair_13(nums):
    for i in range(len(nums)-1):
        if nums[i]==13 and nums [i+1]==13:
            return True 
    return False
    
    
    
nums = [13, 13, 12, 12]
print(pair_13(nums))