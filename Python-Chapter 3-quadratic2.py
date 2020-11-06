# quadratic.py
# A program that computes the real roots of a quadratic equation. Illustrates use of the math library.
# Note: This program crashes if the euqation has no real roots.

import math # Makes the math library available.

def quadratic():
    print ("This program finds the real solutions to a quadractic.")
    print()
    
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discRoot = (b * b - 4 * a * c) ** 0.5
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are:", root1, root2)

quadratic()
    
    
