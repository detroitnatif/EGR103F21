# -*- coding: utf-8 -*-
"""
[Function or Script Name]
[Your Name]
[Date Modified]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [Tk206]
"""


# %% Define function
def hms (secs):
    hrs = secs//3600
    mins = (secs - hrs * 3600 )//60
    secs = secs - (hrs * 3600) - (mins*60)
    return(hrs, mins, secs)

print(hms(3700))

