# futval.py
# A program to compute the value if an investment
# carried 10 years into the future

def futval():
    print ("This program calculates the future value of a mutiple-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    n = eval(input("Future value in year: "))

    for i in range (n):
           principal = principal * (1 + apr)

    print("The value in n years is:", principal)

futval()
    
    
