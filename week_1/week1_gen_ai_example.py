"""
Author: Victoria Edwards
Date: 03/31/2026

Purpose: example code for class

AI Usage statement: This code was generated using ChatGPT
"""

import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)

# Draw sun
t.penup()
t.goto(200, 150)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()

# Draw ocean
t.penup()
t.goto(-400, -50)
t.pendown()
t.color("blue")
t.begin_fill()
for _ in range(2):
    t.forward(800)
    t.right(90)
    t.forward(300)
    t.right(90)
t.end_fill()

# Draw mountains
def draw_mountain(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("gray")
    t.begin_fill()
    t.goto(x + size, y + size * 1.5)
    t.goto(x + size * 2, y)
    t.goto(x, y)
    t.end_fill()

draw_mountain(-250, -50, 100)
draw_mountain(-100, -50, 120)
draw_mountain(80, -50, 90)

# Draw trees
def draw_tree(x, y):
    # trunk
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(10)
        t.left(90)
        t.forward(30)
        t.left(90)
    t.end_fill()
    
    # leaves
    t.penup()
    t.goto(x - 15, y + 30)
    t.pendown()
    t.color("darkgreen")
    t.begin_fill()
    t.goto(x + 5, y + 70)
    t.goto(x + 25, y + 30)
    t.goto(x - 15, y + 30)
    t.end_fill()

for pos in [-200, -150, -50, 0, 100]:
    draw_tree(pos, -50)

# Draw rocky shoreline
t.penup()
t.goto(-400, -50)
t.pendown()
t.color("darkgray")
t.width(3)
for i in range(20):
    t.forward(40)
    t.left(5)

t.hideturtle()
turtle.exitonclick()
