"""
Author: Victoria Edwards
Date: 03/23/2026

Purpose: Test lab 3 ideas
"""

import turtle
import sys

def goto(x, y):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()

# Do this in class
def block(x, y, width, height, fill):
    goto(x, y)
    if fill:
        turtle.begin_fill()
    
    for i in range(4):
        turtle.forward(100 * scale)
        turtle.left(90)

    if fill:
        turtle.end_fill()

# Write a general polygon function
def polygon(x, y, scale, N, fill, color):
    turtle.color(color)
    angle = 360 / N
    goto(x, y)

    if fill:
        turtle.begin_fill()
    
    for i in range(N):
        turtle.forward(100 * scale)
        turtle.left(angle)

    if fill:
        turtle.end_fill()

if __name__ == "__main__":
    polygon(0, 0, 1, 4, True, "red")
    turtle.exitonclick()
