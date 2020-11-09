# coffee.py
# A program that computes the cost of an order. Illustrates use of the math library.

import math # Makes the math library available.

def coffee():
    print ("This program computes the cost of an order.")
    print()

    print ("The cost of per pound = 10.50.")
    print ("The cost of an shipment = 0.86.")
    print ("The cost of fixed cost for overhead = 1.50.")
    print()

    n = int(input("How many pounds: "))
    for i in range (n):
        total = n * 10.5 + 0.86 + 1.50         
    print()
    
    print("The total cost of an order is:", total)

coffee()
