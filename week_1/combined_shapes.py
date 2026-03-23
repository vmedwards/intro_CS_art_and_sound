"""
Author: Victoria Edwards
Date: 03/18/2026
Purpose: Assignment 1
"""

from turtle import *

def star():
    # Star shape
    up()
    forward(100)
    right(20)
    down()
    forward(110)
    left(90)
    
    forward(100)
    right(20)
    forward(100)
    left(90)

    forward(100)
    right(20)
    forward(100)
    left(90)
    
    forward(100)
    right(20)
    forward(100)
    left(90)
    
    forward(100)
    right(20)
    forward(100)
    left(90)
    
    forward(110)
    right(20)

def triangles():
    
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
    right(120)
    up()
    forward(35)
    left(-70)
    down()
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
    right(120)

def shapeC():
    star()
    forward(100)
    triangles()
    
#star()
#triangles()
shapeC()

exitonclick()
