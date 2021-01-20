__author__ = "Arana Fireheart"
from math import pi

class Cubiod(object):
    def __init__(self, startingHeight, startingWidth, startingDepth):
        self.height = float(startingHeight)
        self.width = float(startingWidth)
        self.depth = float(startingDepth)

    def __str__(self):
        return "Height: %5.2f Width: %5.2f Depth: %5.2f" % (self.getHeight(), self.getWidth(), self.getDepth())

    def setWidth(self, newWidth):
        self.width = float(newWidth)

    def getWidth(self):
        return self.width

    def setHeight(self, newHeight):
        self.height = float(newHeight)

    def getHeight(self):
        return self.height

    def setDepth(self, newDepth):
        self.depth = float(newDepth)

    def getDepth(self):
        return self.depth

    def volume(self):
        return self.getHeight() * self.getWidth() * self.getDepth()

    def surfaceArea(self):
        frontSide = self.getHeight() * self.getWidth()
        topSide = self.getDepth() * self.getWidth()
        rightSide = self.getHeight() * self.getDepth()
        return frontSide * 2 + topSide * 2 + rightSide * 2

class Cube(Cubiod):
    def __init__(self, startingWidth, startingHeight = 0, startingDepth = 0):
        if startingHeight == 0 and startingDepth == 0:
            if  startingWidth > 0:
                self.width = self.height = self.depth = float(startingWidth)
            else:
                raise ValueError
        elif startingWidth == startingHeight and startingWidth == startingDepth:
            self.width = self.height = self.depth = float(startingWidth)
        else:
            raise ValueError

class Sphere(object):
    def __init__(self, startingRadius):
        self.setRadius(startingRadius)


    def __str__(self):
        return "Radius: %2.5f Volume: %1.5f Surface Area: %2.5f" %(self.radius, self.volume(), self.surfaceArea())

    def setRadius(self, newRadius):
        if type(newRadius) == int or type(newRadius) == float:
            if newRadius > 0:
                self.radius = float(newRadius)
            else:
                raise ValueError
        else:
            raise ValueError

    def getRadius(self):
        return self.radius

    def volume(self):
        return 4 / 3 * pi * self.getRadius() ** 3

    def surfaceArea(self):
        return 4 * pi * self.getRadius() ** 2


# Test the Cuboid class
#
quad1 = Cubiod(10, 20, 30)
print(quad1)
print(quad1.volume())
print(quad1.surfaceArea())

print(quad1.getHeight())
quad1.setHeight(20)
print(quad1.getHeight())

print(quad1.getWidth())
quad1.setWidth(30)
print(quad1.getWidth())

print(quad1.getDepth())
quad1.setDepth(40)
print(quad1.getDepth())

print(quad1)
print(quad1.volume())
print(quad1.surfaceArea())

# Test the Cube subclass
#
try:
    cube1 = Cube(10, 10, 10)
    print(cube1.volume())
    print(cube1.surfaceArea())
except ValueError:
    print("Usage: All values must be the same.")

try:
    cube1 = Cube(0)
    print(cube1.volume())
    print(cube1.surfaceArea())
except ValueError:
    print("Usage: Values can not be zero.")

try:
    cube2 = Cube(10)
    print(cube2.volume())
    print(cube2.surfaceArea())
except EnvironmentError:
    print("Usage: All values must be the same.")

try:
    cube3 = Cube(10, 20, 30)
    print(cube3.volume())
    print(cube3.surfaceArea())
except ValueError:
    print("Usage: All values must be the same.")

sphere1 = Sphere(3)
print(sphere1.volume())
print(sphere1.surfaceArea())
print(sphere1)
sphere1.setRadius(4)
print(sphere1)
print(sphere1.getRadius())
try:
    sphere2 = Sphere('Hi')
except ValueError:
    print("Usage: Sphere takes only positive integers or floats for radius")
