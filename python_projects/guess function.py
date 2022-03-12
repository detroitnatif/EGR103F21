import numpy as np


def make_prize(low=300, high=600): #get rabdom numbers from numpy 
    return np.random.randint(low, high, 1)

def get_guess ():
    return int(input("guess: "))
if __name__ == '__main__':

    prize = make_prize()
    print(prize)
    guess = get_guess()

    while prize != guess:
        if prize > guess:
            print('higher')
        else:
            print("lower")
    if prize == guess:
        print("Correct!")
guess = get_guess()
   
        
  

