Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import graphics
>>> win = graphics.GraphWin()
>>> win.close()
>>> from graphics import*
>>> win = GraphWin()
>>> p = Point (50,60)
>>> p.getX()
50.0
>>> p.getY()
60.0
>>> win = GraphWin()
>>> p.draw (win)
Point(50.0, 60.0)
>>> p2 = Point (140,100)
>>> p2.draw(win)
Point(140.0, 100.0)
>>> p3 = Point (150, 90)
>>> p3.draw(win)
Point(150.0, 90.0)
>>> ### Open a graphics window
>>> win = GraphWin ('Shapes')
>>> ### Draw a red circle centered at point (100,100) with radius 30
>>> center = Point (100,100)
>>> circ = Circle (center, 30)
>>> circ.setFill ('red')
>>> circ.draw (win)
Circle(Point(100.0, 100.0), 30)
>>> ### Put a textual label in the center of the circle
>>> label = Text (center, "Red Circle")
>>> label.draw (win)
Text(Point(100.0, 100.0), 'Red Circle')
>>> ### Draw a squar using a Rectangle object
>>> rect = Rectangle (Point (30,30), Point(70,70))
>>> rect.draw(win)
Rectangle(Point(30.0, 30.0), Point(70.0, 70.0))
>>> ### Draw a line segment using a Line object
>>> line = Line(Point(20,30), Point(180,165))
>>> line.draw(win)
Line(Point(20.0, 30.0), Point(180.0, 165.0))
>>> ### Draw an oval using the Oval object
>>> oval = Oval (Point (20,150),Point (180,199))
>>> oval.draw(win)
Oval(Point(20.0, 150.0), Point(180.0, 199.0))
>>> circ = Circle (Point(100,100), 30)
SyntaxError: invalid syntax
>>> from graphics import*
>>> circ = Circle (Point(100,100), 30)
>>> win = GraphWin()
>>> circ.draw(win)
Circle(Point(100.0, 100.0), 30)
>>> p = Point (50,70)
>>> p.draw(win)
Point(50.0, 70.0)
>>> p.move(20,10)
>>> 