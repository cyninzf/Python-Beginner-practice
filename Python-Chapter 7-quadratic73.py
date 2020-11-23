# quadratic73.py

import math # Makes the math library available.

def quadratic73():
    print ("This program finds the real solutions to a quadractic.\n")
    
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discrim = b ** 2 - 4 * a * c
    if discrim < 0:
        print("\nThe quation has no real roots!")
    else:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)

    print("\nThe solutions are:", root1, root2)

quadratic73()
