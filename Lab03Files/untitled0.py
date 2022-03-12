#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

def total_seconds(hrs, mins=0, secs=0):
    time = hrs*3600 + mins*60 + secs
    return time


if __name__ == "__main__":
    print(total_seconds(1))
    print(total_seconds(1, 2))
    print(total_seconds(1, 2, 3))
    
if __name__ == "__main__":
    print(total_seconds(1))
    print(total_seconds(1, 2))
    print(total_seconds(1, 2, 3))
 



     


