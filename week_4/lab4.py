"""
Author: Victoria Edwards
Date: 03/24/2026

Purpose: Lab 4 testing
"""

# description: 
from earsketch import *
import random as rand

# Task 1 write a soundBite1 function
def soundBite1():
    # load media using the fitMedia function
    # Do this for them

def soundBite2():
    # Do something with if statements

def soundBite3(): 
    

def soundBite(track_a, track_b):
    for i in range(1, 11, 4):  
        sound = selectRandomFile(ALT_POP_GUITAR)
        print(i, i + 2)
        fitMedia(sound, track_a, i, i +4)

        r = rand.choice([0, 1])
        if r: 
            fitMedia(YG_FUNK_HIHAT_2, track_b, i + 1, i + 3)
        else:
            fitMedia(RD_POP_TB303LEAD_3, track_b, i + 1, i + 3)

if __name__ == "__main__":
    setTempo(120)
    soundBite(1, 2)
    soundBite(3, 4)

    
