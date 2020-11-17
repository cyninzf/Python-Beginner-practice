# futval_graph2.py

from graphics import*

def futval_graph2():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("light blue")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(20,230), '0.0K').draw(win)
    Text(Point(20,180), '2.5K').draw(win)
    Text(Point(20,130), '5.0K').draw(win)
    Text(Point(20,80), '7.5K').draw(win)
    Text(Point(20,30), '10.0K').draw(win)

    # Draw bar for initial principal
    bar = Rectangle(Point(0,0),Point(1, principal))
    bar.setFill("purple")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range (1,11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("purple")
        bar.setWidth(3)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

futval_graph2()

        
        
    
