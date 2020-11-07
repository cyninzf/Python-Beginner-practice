# cost.py
# A program that computes the cost per square inch of a circular pizza given its diameter and price. Illustrates use of the math library.

import math # Makes the math library available.

def cost():
    print ("This program computes the cost per square inch of a circular pizza.")
    print()
    
    price = float(input("Enter price: "))
    D = float(input("Enter diameter in inch D: "))
    R = D / 2
    A = math.pi * (R ** 2)
    cost = price / A
             
    print()
    print("The cost per square inch is:", cost)

cost()
