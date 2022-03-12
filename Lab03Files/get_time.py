#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[Get_time.py]
[Tyler Klimas]
[9-11-2021]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [Tk206]
"""

def total_seconds(hrs, mins=0, secs=0):
    time = hrs*3600 + mins*60 + secs
    return time


if __name__ == "__main__":
    print(total_seconds(1))
    print(total_seconds(1, 2))
    print(total_seconds(1, 2, 3))
 



     


