# speed.py
# A program that computes the distance to a lightning strike 
# based on the time elapsed between the flash and the sound of thunder.
# llustrates use of the math library.

import math # Makes the math library available.

def speed():
    print ("This program computes the distance to a lightning strike.")
    print()
    print ("This speed of sound is approximately 1100 ft/sec and 1 mile is 5280 ft.")
    print()
    
    S = float(input("Enter the number of second S: "))
    distance = S * 1100

    print()
    print("The distance in feet to a lightning strike is:", distance, "ft")
    print("The distance in mile to a lightning strike is:", distance / 5280, "mi")

speed()
