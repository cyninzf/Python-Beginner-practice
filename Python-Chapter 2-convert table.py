# convert.py
# A program to convert Celsius to Fahrenheit
# by: cynxinzf

def convertable():
    print("This program convert Celsius to Fahrenheit.")

    for i in range (10):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
    
        print("Celsius degrees = ",celsius,";" "Fahrenheit degrees = ", fahrenheit)

convertable ()

