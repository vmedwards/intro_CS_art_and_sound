"""
Author: Victoria Edwards
Date: 04/06/2026

Purpose: do more with turtle
"""
import turtle

def fillTriangle(distance, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    triangle(distance, 120)
    turtle.end_fill()


def triangle(distance, angle):
    # angle = 120
    
    # this is for a triangle in class ES1098
    # we now want to do something else 

    turtle.forward(distance)
    turtle.left(angle)
    turtle.forward(distance)
    turtle.left(angle)
    turtle.forward(distance)
    turtle.left(angle)
    

triangle(100, 120)
fillTriangle(200, "red")    
turtle.exitonclick()
