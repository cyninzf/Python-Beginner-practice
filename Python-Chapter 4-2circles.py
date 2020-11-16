Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import graphics
>>> from graphics import*
>>> # A correct way to create two circles
>>> leftEye = Circle (point(80,50),5)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    leftEye = Circle (point(80,50),5)
NameError: name 'point' is not defined
>>> leftEye = Circle (Point(80,50),5)
>>> win = GraphWin ()
>>> leftEye.setFill ('yellow')
>>> # A correct way to create two circles
>>> win = GraphWin()
>>> leftEye = Circle(Point(80,50),5)
>>> leftEye.setFill('yellow")
		
SyntaxError: EOL while scanning string literal
>>> leftEye.setFill('yellow')
>>> leftEye.draw(win)
Circle(Point(80.0, 50.0), 5)
>>> leftEye.setOutline('red')
>>> rightEye = Circle(Point(100,50),5)
>>> rightEye.setFill('red')
>>> rightEye.setOutline('yellow')
>>> rightEye.draw(win)
Circle(Point(100.0, 50.0), 5)
>>> 