# convert.py
# A program to convert Celsius to Fahrenheit
# by: cynxinzf

def convert():
    print("This program convert Celsius to Fahrenheit.")

    for i in range (5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
    
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        input("Press the Enter key to quit.")

convert ()

