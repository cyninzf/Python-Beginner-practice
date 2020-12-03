# launcher.py

"""Chapter 11 - the launcher widget will show a cannonball ready to be
launched along with an arrow representing the current settings for the
launch angle and velocity."""

from math import sin, cos, radians
from random import randrange

class Launcher:

    def adjAngle(self, amt):
        """change launch angle by amt degree."""
        
        self.angle = self.angle + radians(amt)
        self.redraw()

    def adjVel(self, amt):
        """change launch velocity by amt degree."""
        
        self.vel = self.vel + amt
        self.redraw()

    def redraw(self):
        """ readraw the arrow to show current angle and velocity"""
        
        self.arrow.undraw()
        pt2 = Point(self.vel*cos(self.angle),
                    self.vel*sin(self.angle))
        self.arrow = Line(Point(0,0), pt2).draw(Self.win)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)

    def fire(self):
        return ShortTracker(self.win, degrees(self.angle), self.vel, 0.0)

    def __init__(self,win):
        # draw the base shot of the launcher
        base = Circle(Point(0,0), 3)
        base.setFill("red")
        base.setOutline("black")
        base.draw(win)

        # save the window and create initial angle and velocity
        self.win = win
        slef.angle = radians(45.0)
        self.vel = 40.0

        # create initial "dummy" arrow (needed by redraw)
        self.arrow = Line(Point(0,0), Point(0,0)).draw(win)
        # replace it with the correct arrow
        self.redraw()
        
        
