# distance7.py
# A program that calculates the distance between two (non-vertical) points entered by the user.
# Illustrates use of the math library.

import math # Makes the math library available.

def distance7():
    print ("This program calculates the distance between two non-vertical points")
    print()
    
    x1 = float(input("Enter coordinate x1: "))
    x2 = float(input("Enter coordinate x2: "))
    y1 = float(input("Enter coordinate y1: "))
    y2 = float(input("Enter cooridnate y2: ")) 

    distance = math.sqrt ((x2-x1) ** 2 + (y2-y1) ** 2)      
    print()
    
    print("The distance is:", distance)

distance7()
