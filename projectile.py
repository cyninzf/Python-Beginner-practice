# projectile.py

"""updating projectile.py
provides a simple class for modeling the flight of projectiles."""

from math import sin, cos, radians

class Projectile:

    """Simulates the flight of simple projectiles near the earth's surfaces,
    ignoring wind resistance. Tracking is done in two dimensions, height (y)
    and distance (x)."""

    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, dt):
        """Update the short dt seconds farther along its flight."""

        # update the projectile
        self.proj.update(dt)

        # move the circle to the new projectile location
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)

    def getX(self):
        """ Returns the current x coordinate of the shot's center."""
        return self.proj.getX()

    def getY(self):
        """ Returns the y coordinate of the shot's center."""
        return self.proj.getY()

    def undraw(Self):
        """ undraw the shot """
        self.marker.undraw()
