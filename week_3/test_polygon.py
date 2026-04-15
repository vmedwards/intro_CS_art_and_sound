"""
Author: Victoria Edwards
Date: 03/23/2026

Purpose: Test assignment 3
"""

import turtle
import sys
import betterShapelib as shape

# Define a repeating pattern
def repeating_pattern(N, polySide, x = 0, y = 0, fill = True, scale_x = None, scale_y = None):
    turtle.colormode(255)
    c1 = (255, 255, 0)

    # Get non-user specified values
    if scale_x is None and scale_y is None: 
        scale_x = (polySide - 3) * 4 + 10
        scale_y = (polySide - 3) * 4 + 10


    # Nest loops to get a grid of locations
    for i in range(N):
        for j in range(N):
            color = (int(c1[0] - 255 / (i + 1)), int(c1[1] - 255 / (j + 1)), int(c1[2] + 255 / (i + 1)))
            print(color)
            turtle.color(color)
            shape.polygon(x + i * scale_x, y + (j + 1) * scale_y, 0.1, polySide, fill = fill)

def main(): 
    turtle.tracer(False)
    # Draw one filled and one unfilled shape pattern
    repeating_pattern(10, 10, -200, -200, fill = False)
    repeating_pattern(10, 4, -200, -200, scale_x = 38, scale_y = 39)
    turtle.update()
    turtle.mainloop()

if __name__ == "__main__":
    main()
