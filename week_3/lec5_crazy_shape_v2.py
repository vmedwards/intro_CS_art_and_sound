"""
Author: Victoria Edwards
Date: 04/14/2026

Purpose: Show example of how to debug with turtle graphics
"""

import random as rand
import turtle

turtle.colormode(255)

def crazyShape(num_iter, num_no_fill, num_fill):
    turtle.color((rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255)))

    screen = turtle.Screen()
    width = screen.window_width()
    height = screen.window_height()
    
    for _ in range(num_iter): 
        for i in range(num_no_fill):
            x, y = turtle.position()
            #if x > width or y > height or x < 0 or y < 0:
            #    turtle.goto(rand.randint(0, 100), rand.randint(0, 100))
            turtle.forward(rand.randint(0, 100))
            turtle.left(rand.randint(-360, 360))

        turtle.begin_fill()
        for j in range(num_fill):
            #if x > width or y > height or x < 0 or y < 0:
            #    turtle.goto(0, 0)
            turtle.forward(rand.randint(10, 200))
            turtle.left(rand.randint(-360, 360))
        turtle.end_fill()

        

def crazyShapeRainbow(num_iter, num_no_fill, num_fill):
    screen = turtle.Screen()
    width = screen.window_width()
    height = screen.window_height()
    
    for _ in range(num_iter): 
        for i in range(num_no_fill):
            turtle.color((rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255)))

            x, y = turtle.position()
            #if x > width or y > height or x < 0 or y < 0:
            #    turtle.goto(rand.randint(0, 100), rand.randint(0, 100))
            turtle.forward(rand.randint(0, 100))
            turtle.left(rand.randint(-360, 360))

        turtle.begin_fill()
        for j in range(num_fill):
            turtle.color((rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255)))

            #if x > width or y > height or x < 0 or y < 0:
            #    turtle.goto(0, 0)
            turtle.forward(rand.randint(10, 200))
            turtle.left(rand.randint(-360, 360))
        turtle.end_fill()
    
def example1(num_drawings): 
    turtle.tracer(False)
    for i in range(num_drawings):
        crazyShape(10, 5, 2)
    turtle.update()
    turtle.mainloop()

def example2(num_drawings):
    turtle.tracer(False)
    for i in range(num_drawings):
        crazyShapeRainbow(10, 2, 5)
    turtle.update()
    turtle.mainloop()

def example3(num_drawings):
    turtle.tracer(False)
    for i in range(num_drawings):
        coinFlip = rand.randint(0, 1)
        if coinFlip:
            crazyShapeRainbow(10, 2, 5)
        else:
            crazyShape(10, 2, 5)
    turtle.update()
    turtle.mainloop()

example1(10)
#example2(5)
#example3(2)
