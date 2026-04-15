"""
Author: Victoria Edwards
Date: 04/09/2026

Purpose: Turtle graphic for loop example
"""

import turtle


# What shape is this? 
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
    print("The loop index is: ", i)

for side in range(4):
    turtle.forward(100)
    turtle.left(90)
    print("the loop index for the square is: " + str(side))

turtle.exitonclick()
                   
