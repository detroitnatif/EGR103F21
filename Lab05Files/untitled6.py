#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:15:12 2021

@author: tylerklimas
"""

from chapra_0304 import daily_temp 
import matplotlib.pyplot as plt
import numpy as np


miami_days = daily_temp('Miami', np.arange(0, 366))
yuma_days = daily_temp('Yuma', np.arange(0, 366))
bismarck_days = daily_temp('Bismarck', np.arange(0, 366))
seattle_days = daily_temp('Seatlle', np.arange(0, 366))
boston_days = daily_temp('Boston', np.arange(0, 366))
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1)
