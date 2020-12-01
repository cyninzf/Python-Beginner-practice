# ShotTracker.py

def __init__(self, win, angle, velocity, height):
    """win is the GraphWin to display the shot. angle, velocity, and height are
    initial projectile parameters."""

    self.proj = Projectile(angle, velocity, height)
    self.marker = Circle(Point(0,height), 3)
    self.marker.setFill("red")
    self.marker.setOutline("red")
    self.marker.draw(win)
