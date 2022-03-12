import numpy as np
import math as m 

def daily_temp(city, days):
    """
    DailyTemp  Calculate temperatures for a city.
      daily_temp(city, days)
      city: a string containing a city name
      days: an array of any size with values denoting day
            of the year
      Returns: an array with the predicted temperatures for 
            the given city on the given days
[chapra_0304.py]
[Tyler Klimas]
[9-19-21]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [TK206]
"""
    # Use dictionary to store city mean/peak Temps
    
    tdict = {}
    tdict["Miami"] = (22.1, 28.3)
    tdict['Yuma'] = (24.9, 33.6)
    tdict['Bismarck'] = (5.2, 22.1)
    tdict['Seattle'] = (10.6, 17.6)
    tdict['Boston'] = (10.7, 22.9)
    tdict['Durham'] = (15.7, 31)
    # complete this table

    # Use formula to calculate array of temperatures
    peak_day = 205
    t = days
    tmean = tdict[city][0]
    tpeak = tdict[city][1]
    temp = tmean + (tpeak - tmean)*np.cos((2*(np.pi))/365 * (np.array(t) - 205))
    return temp

print(np.mean(daily_temp('Yuma', np.arange(0,59))))
print(np.mean(daily_temp('Seattle', np.arange(180, 242))))