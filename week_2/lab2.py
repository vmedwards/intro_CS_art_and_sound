"""
Author: Victoria Edwards
Date: 03/23/2026
Purpose: Lab 2 for intro to CS

source: https://cs.colby.edu/hewolfe/courses/cs151/f21/projects/02/Lab02FunctionsToControlShapes.html
"""

# IMPORT STATEMENTS

import turtle

# All your self defined functions

def triangle(sideLength):
    """
    draw a triangle with parameter sidelength
    """
    turtle.forward(sideLength)
    turtle.left(120)
    turtle.forward(sideLength)
    turtle.left(120)
    turtle.forward(sideLength)
    turtle.left(120)

def goto(x, y):
    turtle.penup()
    print(turtle.position())
    turtle.goto(x, y)
    print(turtle.position())
    turtle.pendown()

def triangle2(x, y, scale):
  '''
  Draws a triangle at any (`x`, `y`) position and scale (`scale`)
    By default, the side lengths are 100 (when `scale` = 1)
    '''    
  goto(x, y)
  triangle(100 * scale)

def triangleStack(x, y, scale):
    '''Draws three triangles on top of each other.
    Smaller triangles are placed on top of larger ones
    '''
    # Largest triangle
    triangle2(0 + x, 0 + y, 2 * scale)
    # Medium triangle in middle
    triangle2(50 * scale + x, 173.2 * scale + y, 1 * scale)
    # Small triangle on top of stack
    triangle2(75 * scale + x, 259.81 * scale + y, 0.5 * scale)
  
# Main code

# Move the turtle faster (or draw instantly)
turtle.speed(0)

# TASK 3 
#triangle(100)
#goto(100, 100)
#triangle(10)

#goto(0, 100)
#triangle(50)

# TASK 4
triangle2(0, 0, 1)
triangle2(-50, -50, 2)
triangle2(-100, -100, 3)


# TASK 5b
#triangleStack(-200, 0, 1)
#triangleStack(0, 0, 1)
#triangleStack(200, 0, 1)


# TASK 5c
#triangleStack(-200, 0, 1)
#triangleStack(0, 0, 0.5)
#triangleStack(100, 0, 0.3)


# Keep turtle screen open
turtle.exitonclick()
