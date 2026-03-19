"""
Author: Victoria Edwards
Date: 03/18/2026

This is me playing with ideas for final project
"""

import cv2
import numpy as np
import math

def load_image():
    # Read an image from file
    img = cv2.imread('IMG_3206.jpg')
    resized_img = cv2.resize(img,None, fx = 0.2, fy = 0.2, interpolation=cv2.INTER_LINEAR)
    
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    
    # Save the grayscale image
    cv2.imwrite('image_gray.jpg', gray_img)

    edges = cv2.Canny(gray_img, 200, 100)

    img_neg = cv2.bitwise_not(edges)

    # Display the image in a window
    cv2.imshow('Original Image', resized_img)
    cv2.imshow('Canny Edges', edges)
    cv2.imshow('outline', img_neg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

def polar(filename):
    img = cv2.imread(filename)
    img = cv2.resize(img,None, fx = 0.2, fy = 0.2, interpolation=cv2.INTER_LINEAR)

    h, w = img.shape[:2]

    # Center of transformation
    center = (w // 2, h // 2)
    max_radius = min(center[0], center[1], w - center[0], h - center[1])

    # WARP_POLAR_LINEAR converts to polar, WARP_FILL_OUTLIERS handles gaps
    polar_img = cv2.warpPolar(img, (max_radius, 360), center, max_radius, 
                              cv2.WARP_POLAR_LINEAR + cv2.WARP_FILL_OUTLIERS)

    # Rotate if necessary (skyline often looks better rotated)
    polar_img = cv2.rotate(polar_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('Polar Skyline', polar_img)
    cv2.imshow('test', img)
    cv2.waitKey(0)


def skyline(filename):

    pano = cv2.imread(filename)
    pano = cv2.resize(pano, None, fx = 0.2, fy = 0.2, interpolation=cv2.INTER_LINEAR)
    if pano is None:
        print(f"Error: Could not load image from {image_path}")
        return

    height, width, _ = pano.shape

    # Desired size for the output (tiny planet) image
    # The output is typically a square, often twice the height of the original for best results
    # and to fit the entire planet within the frame with surrounding space.
    # The diameter of the planet will be the original image height.
    planet_diameter = height
    planet_radius = height // 2
    planet_size = height  

    # Create a blank square canvas for the tiny planet
    planet_image = np.zeros((planet_size, planet_size, 3), dtype=np.uint8)

    # Pre-calculate constants
    # Longitude (theta) ranges from -PI to PI
    # Latitude (phi) ranges from -PI/2 to PI/2
    
    # Coordinates for mapping (map_x, map_y)
    map_x = np.zeros((planet_size, planet_size), dtype=np.float32)
    map_y = np.zeros((planet_size, planet_size), dtype=np.float32)

    # Loop over every pixel in the target planet image
    for y in range(planet_size):
        for x in range(planet_size):
            # Convert target pixel coordinates to Cartesian coordinates relative to center
            # Center is at (planet_size / 2, planet_size / 2)
            nx = x - planet_size // 2
            ny = y - planet_size // 2

            # Calculate distance from center (r)
            r = math.sqrt(nx*nx + ny*ny)
            
            # Skip pixels outside the planet's circle to add blank corners
            if r > planet_radius:
                continue

            # Calculate polar coordinates (theta, phi)
            # theta (longitude) ranges from -PI to PI
            theta = math.atan2(ny, nx) 
            # phi (latitude) ranges from PI/2 to -PI/2
            phi = math.pi / 2 - math.pi * r / planet_radius

            # Convert polar coordinates to original panorama pixel coordinates (u, v)
            # u (x in pano) ranges from 0 to width
            u = (theta + math.pi) * width / (2 * math.pi)
            # v (y in pano) ranges from 0 to height
            v = (phi + math.pi / 2) * height / math.pi

            # Assign mapping values (OpenCV uses floating point maps for sub-pixel interpolation)
            # Ensure coordinates are within bounds
            if 0 <= u < width and 0 <= v < height:
                map_x[y, x] = u
                map_y[y, x] = v

    # Use cv2.remap to apply the transformation
    # INTER_CUBIC provides a good balance of quality and speed, but others work too
    tiny_planet = cv2.remap(pano, map_x, map_y, cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))

    # Optional: Flip the image vertically so the "ground" is right side up
    # This is a common step in the "tiny planet" workflow
    tiny_planet = cv2.flip(tiny_planet, 0) # Flip around the x-axis (vertically)

    # Display the result
    cv2.imshow("Tiny Planet", tiny_planet)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def real_time_response():

    pass

if __name__ == "__main__": 
    #load_image()
    #polar("IMG_8023.jpg")
    #polar("IMG_7708.jpg")
    #polar("IMG_7592.jpg")

    skyline("IMG_8023.jpg")
    skyline("IMG_7708.jpg")
    skyline("IMG_7592.jpg")
