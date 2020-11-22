# futval_graph4.py

from graphics import*

def createLabeledWindow():
    window = GraphWin("Investment Growth Chart", 640, 480)
    window.setBackground("light blue")
    window.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(20,230), '0.0K').draw(window)
    Text(Point(20,180), '2.5K').draw(window)
    Text(Point(20,130), '5.0K').draw(window)
    Text(Point(20,80), '7.5K').draw(window)
    Text(Point(20,30), '10.0K').draw(window)
    return window

def drawBar(window,year, height):
    # Draw a bar in window starting at year with given height
    bar = Rectangle(Point(year,0),Point(year+1, height))
    bar.setFill("purple")
    bar.setWidth(2)
    bar.draw(window)

def futval_graph4():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    win = createLabeledWindow()
    drawBar(win, 0, principal)
    for year in range (1,11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        drawBar(win, year, principal)

    input("Press <Enter> to quit")
    win.close()

futval_graph4()

        
        
    
