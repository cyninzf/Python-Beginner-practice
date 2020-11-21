# printfile.py
# Prints a file to the screens.

def printfile():
    fname = input("Enter filename: ")
    infile = open(fname,"r")
    data = infile.read()
    print(data)

printfile()
