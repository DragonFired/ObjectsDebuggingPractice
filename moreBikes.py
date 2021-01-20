#!/usr/bin/env python

class Bicycle(object):

    def __init__(self, cadence = 0, speed = 0, gear = 1):
        self.cadence = cadence
        self.speed = speed
        self.gear = gear

    def changeCadence(self, newValue):
        self.cadence = newValue

    def getCadence(self):
        return self.cadence

    def changeGear(self, newValue):
        self.gear = newValue

    def getGear(self):
        return self.gear

    def speedUp(self, increment):
        self.speed += increment

    def getSpeed(self):
        return self.speed

    def applyBrakes(self, decrement):
        self.speed -= decrement

    def __str__(self):
        return "cadence: {0} speed: {1} gear: {2}".format(self.getCadence(), self.getSpeed(), self.getGear())

class ThreeSpeedBike(Bicycle):
    NUMGEARS = 3
    def changeGear(self,  newValue):
        if 0 < newValue < self.NUMGEARS + 1:
            self.gear = newValue
        else:
            print("This bike has only %i gears. You cannot set the gear to %i" % (self.NUMGEARS,  newValue))
            
# BicycleDemo

# Create three different Bicycle objects
bike1 = Bicycle()
bike2 = Bicycle()
bike3 = ThreeSpeedBike()

# Invoke methods on those objects
print("Bike1")
bike1.changeCadence(50)
bike1.speedUp(10)
bike1.changeGear(2)
print(bike1)

print("Bike2")
bike2.changeCadence(50)
bike2.speedUp(10)
bike2.changeGear(2)
bike2.changeCadence(40)
bike2.speedUp(10)
bike2.changeGear(3)
print(bike2)

print("Bike3")
bike3.changeCadence(50)
bike3.speedUp(10)
bike3.changeGear(4)
bike3.changeCadence(40)
bike3.speedUp(10)
bike3.changeGear(3)
bike3.changeGear(0)
print(bike3)
print(bike3)