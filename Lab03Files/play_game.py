# -*- coding: utf-8 -*-
"""
[Function or Script Name]
[Your Name]
[Date Modified]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [Your NetID]
"""
# %% Import modules
import numpy as np


# %% Define function
def roll_dice(n_dice=1, n_sides=6, seed=0):
    np.random.seed(seed)
    
    rollresults=[]
    rollcount=[]
    for i in range(n_sides):
        rollcount.append(0)
    
    for i in range(n_dice):
        rollresults.append(np.random.randint(1,n_sides+1))
        
    for i in range(n_dice):
        rollcount[rollresults[i]-1]+=1
        
    return rollresults, rollcount

if __name__ == "__main__":
    print(roll_dice(10,6))