Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## Correct way to create two circles, using clone.
>>> import graphics
>>> from graphics import*
>>> win = GraphWin()
>>> letfEye = Circle(Point(80,50),5)
>>> leftEye.setFill('blue')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    leftEye.setFill('blue')
NameError: name 'leftEye' is not defined
>>> leftEye = Circle(Point(80,50),5)
>>> leftEye.draw(win)
Circle(Point(80.0, 50.0), 5)
>>> letfEye.setFill('blue')
>>> leftEye.setOutline('yellow')
>>> leftEye.setFill('green')
>>> rightEye = leftEye.clone()
>>> # rightEye is an exact copy of the left
>>> rightEye.move(20,0)
>>> rightEye.draw(win)
Circle(Point(100.0, 50.0), 5)
>>> 