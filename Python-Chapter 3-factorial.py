# factorial.py
# Program to compute the factorial of a number. Illustrates for loop with an accumulator.

import math # Makes the math library available.

def factorial():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

factorial()
    
    
