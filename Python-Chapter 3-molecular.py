# molecular.py
# A program that computes the molecular weight of a carbohydrate (in grams per mole)
# based on the number of hydrogen, carbon, and oxygen atoms in the molecule.
# llustrates use of the math library.

import math # Makes the math library available.

def molecular():
    print ("This program computes the molecular weight of a carbohydrate (in grams per mole).")
    print()

    print ("The formular of carbohydrate = C(H2O)")
    print()
    H = float(input("Enter the number of hydrogen atmos H: "))
    C = float(input("Enter the number of carbon atmos C: "))
    O = float(input("Enter the number of oxygen atmos O: "))
    
    total = C + H * 2 + O     

    print()
    print("The total combined molecular weight of all the atmos is:", total)

molecular()
