__author__ = 'arana'
from math import sqrt

class Rectangle(object):
    """This class represents a four sided 2D shape."""
    def  __init__(self, newWidth, newHeight):
        self.width = newWidth
        self.height = newHeight

    def __str__(self):
        return "Height: {0} Width: {1}i Area: {2} Perimiter: {3} Diagonal: {4:5.2f}".format(self.getHeight(), self.getWidth(), self.area(), self.perimeter(), self.diagonal())

    def getWidth(self):
        return self.width

    def setWidth(self, changeWidth):
        self.width = changeWidth

    def getHeight(self):
        return self.height

    def setHeight(self, changeHeight):
        self.height = changeHeight

    def area(self):
        return self.getWidth() * self.getHeight()

    def perimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

    def diagonal(self):
        return sqrt(self.getWidth() ** 2 + self.getHeight() ** 2)

rectangle1 = Rectangle(50, 10)
print(rectangle1.area())		# Prints 500
print(rectangle1.perimeter())	# Prints 120
print("%2.4f" % rectangle1.diagonal())    # Prints 50.990153592785
print(rectangle1)
rectangle1.setHeight(30)
print(rectangle1)
print(rectangle1.getHeight())