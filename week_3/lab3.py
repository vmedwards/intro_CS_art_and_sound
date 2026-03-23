"""
Author: Victoria Edwards
Date: 03/23/2026

Purpose: Test lab 3 ideas
"""

import turtle

def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def square(x, y, scale):
    goto(x, y)
    for i in range(4):
        turtle.forward(100 * scale)
        turtle.left(90)


def complex_pattern(N):
    for i in range(N):
        for j in range(N):
            square(i * 20, j * 20, 0.1)


if __name__ == "__main__":
    turtle.speed(0)
    complex_pattern(10)
