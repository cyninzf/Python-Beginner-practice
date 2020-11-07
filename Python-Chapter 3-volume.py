# volume.py
# A program that computes the volume and surface area of a sphere from its radius. Illustrates use of the math library.

import math # Makes the math library available.

def volume():
    print ("This program computes the volume and surface area of a sphere.")
    print()
    
    r = float(input("Enter radium r: "))
    v = 4 / ((3 * math.pi)* (r**3))
    a = 4 * math.pi * (r**2)
             
    print()
    print("The volume is:", v)
    print("The surface area is:", a)

volume()
