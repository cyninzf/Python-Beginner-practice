# slope.py
# A program that calculates the slope of a line through two (non-vertical) points entered by the user.
# Illustrates use of the math library.

import math # Makes the math library available.

def slope():
    print ("This program calculates the slope of a line through two non-vertical points")
    print()
    
    x1 = float(input("Enter coordinate x1: "))
    y1 = float(input("Enter coordinate y1: "))
    x2 = float(input("Enter coordinate x2: "))
    y2 = float(input("Enter cooridnate y2: ")) 
    slope = (y2-y1) / (x2-x1)         
    print()
    
    print("The slope is:", slope)

slope()
