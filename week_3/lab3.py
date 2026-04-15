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
def square(x, y, scale):
    goto(x, y)
    for i in range(4):
        turtle.forward(100 * scale)
        turtle.left(90)

# Write a general polygon function
def polygon(x, y, scale, N):
    angle = 360 / N
    goto(x, y)
    for i in range(N):
        turtle.forward(100 * scale)
        turtle.left(angle)

# draw a star with the given number of rays of the given size
def star( rays, size ):
    print("Drawing a star with", rays, "rays of size", size )
    # loop for the number of rays
    for i in range(rays):
        print(i)
        turtle.setheading( i * 360 / rays )
        turtle.forward( size )
        turtle.backward( size )
        

# Define a repeating pattern
def repeating_pattern(N, polySide, c1, x = 0, y = 0):
    turtle.colormode(255)
    scale = (polySide - 3) * 3 + 10
    for i in range(N):
        for j in range(N):
            color = (int(c1[0] - 255 / (i + 1)), int(c1[1] - 255 / (j + 1)), int(c1[2] + 255 / (i + 1)))
            #color = (int(c1[0] - 255 / (j + 1)), int(c1[1] - 255 / (i + 1)), int(c1[2] + 255 / (i + 1)))
            print(color)
            turtle.color(color)

            #square(i * 20, j * 20, 0.1)
            turtle.begin_fill()
            polygon(x + i * scale, y + j * scale, 0.1, polySide)
            turtle.end_fill()

def main():
    #turtle.speed(0)
    turtle.tracer(False)
    # assign values to variables

    numrays = 10
    raysize = 100
    if len(sys.argv) > 2:
        numrays = int(sys.argv[1])#10
        raysize = int(sys.argv[2]) #50
    
    # call the star function
    for i in range(-200, 200, 50): 
        turtle.penup()
        turtle.goto(i, 0)
        turtle.pendown()
        star(numrays, raysize)
    
    #repeating_pattern(4, 4, (255, 255, 0))
    #repeating_pattern(10, 5, (255, 255, 0), 50, 50)
    turtle.update()
    turtle.mainloop()

    

if __name__ == "__main__":
    main()
