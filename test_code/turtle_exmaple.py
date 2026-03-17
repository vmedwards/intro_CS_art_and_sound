import turtle

# --- Configuration ---
WIDTH, HEIGHT = 600, 600
# Define the complex plane boundaries
RE_START, RE_END = -2.0, 1.0
IM_START, IM_END = -1.0, 1.0
MAX_ITERATIONS = 100

def mandelbrot_color(c):
    """
    Checks if a point c is in the Mandelbrot set and returns a color value.
    """
    z = 0j # Python handles complex numbers natively
    for i in range(MAX_ITERATIONS):
        z = z*z + c
        if abs(z) >= 2.0: # The sequence is not bounded if the modulus > 2
            # Return an integer value to be mapped to a color
            return i
    return -1 # Indicates the point is likely within the set (black)

def draw_mandelbrot():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT) # Map screen pixels to coordinates
    screen.tracer(0, 0) # Turn off automatic animation for speed

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed('fastest')

    for x in range(WIDTH):
        # Scale pixel x to real coordinate
        real_part = RE_START + (x / WIDTH) * (RE_END - RE_START)
        for y in range(HEIGHT):
            # Scale pixel y to imaginary coordinate
            imaginary_part = IM_START + (y / HEIGHT) * (IM_END - IM_START)
            c = complex(real_part, imaginary_part)

            iterations = mandelbrot_color(c)

            # Assign color based on iterations
            if iterations == -1:
                color = "black" # Points in the set are black
            else:
                # Simple coloring: shade based on escape time (can be customized)
                # Modulo 255 for basic color cycling
                color_value = iterations % 255
                # Map to a simple grayscale for demonstration
                color = (color_value, color_value, color_value)

            # Turtle needs colors in a specific mode if using tuples (0-255)
            screen.colormode(255)
            t.goto(x, y)
            t.dot(2, color) # Draw a dot at the pixel location

        # Optional: Update the screen periodically to see progress
        if x % 20 == 0:
            screen.update()

    screen.update() # Final update to show the complete image
    screen.exitonclick() # Pause until user clicks in the window

if __name__ == "__main__":
    draw_mandelbrot()
