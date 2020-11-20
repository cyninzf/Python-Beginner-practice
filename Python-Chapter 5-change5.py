# change5.py
# A program to calculate the value of some change in dollars

def change5():
    print ("Change counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    total = quarters * 0.25 + dimes *0.10 + nickels * 0.05 + pennies * 0.01

    print("The total value of your change is ${0:0.2f}:". format(total))

change5()
    
    
