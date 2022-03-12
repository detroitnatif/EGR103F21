#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:19:13 2021

@author: tylerklimas
"""

phrase = 'shaohvpincanceiuebubfcoiOOOer' #input any phrase to use to count

counts = [0, 0, 0, 0, 0] #start with 0s to start count for each variable
vowels = 'aeiou'

for letter in phrase.lower():  #for loop to go through phrase  #writing for only when there is a
    for n, v in enumerate(vowels): # n is postion, v is letter
        if letter == v:  #when v is correct letter, it adds to correct row of 'counts'
            counts[n] += 1 
            break 

        
print(counts)
    
    



