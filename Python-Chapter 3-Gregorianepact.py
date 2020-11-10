# epact.py
# Gregorian epact is a program that calculates the days between Jan. 1st and the previous new moon.
# This value is used to figure out the date of Easter.
# Illustrates use of the math library.

import math # Makes the math library available.

def epact():
    print ("This program calculates the days between Jan. 1st and the previous new moon")
    print()
    
    year = int(input("Enter the # of years: "))
    C = year // 100
    
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30      
    print()
    
    print("The days are:", epact)

epact()
