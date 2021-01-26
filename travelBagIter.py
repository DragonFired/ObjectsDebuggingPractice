__author__ = 'Arana Fireheart'

suitcaseMinimunSize = 1.5 # Smallest suitcase configurable in cubic liters
suitcaseMaximumSize = 20 # Largest suitcase configurable in cubic liters


class LatLong(object):
    def __init__(self):
        self.validLatDirections = ("N", "S")
        self.validLongDirections = ("E", "W")
        self.degrees = 0.0
        self.minutes = 0.0
        self.seconds = 0.0
        self.compassDirection = None

    def __str__(self):
        return f"{self.getDegrees()} {self.getMinutes()} {self.getSeconds()}{self.getCompassDirection()}"

    def getDegrees(self):
        return self.degrees

    def getMinutes(self):
        return self.minutes

    def getSeconds(self):
        return self.seconds

    def getCompassDirection(self):
        return self.compassDirection


class Latitude(LatLong):
    def __init__(self, headingString=""):
        super().__init__()
        self.stringToLatitude(headingString)

    def __str__(self):
        return f"Lat: {super().__str__()}"

    def stringToLatitude(self, inputString):
        if inputString[-1] in self.validLatDirections:
            direction = inputString[-1]
            degrees, minutes, seconds = inputString[:-1].split(' ')
        elif inputString[0] in self.validLatDirections:
            direction = inputString[0]
            degrees, minutes, seconds = inputString[1:].split(' ')
        else:
            raise ValueError
        dMS = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
        if 0 <= dMS <= 90:
            self.degrees = float(degrees)
            self.minutes = float(minutes)
            self.seconds = float(seconds)
            self.compassDirection = direction.upper()
        else:
            raise ValueError


class Longitude(LatLong):
    def __init__(self, headingString=""):
        super().__init__()
        self.stringToLongitude(headingString)

    def __str__(self):
        return f"Long: {super().__str__()}"

    def stringToLongitude(self, inputString):
        if inputString[-1] in self.validLongDirections:
            direction = inputString[-1]
            degrees, minutes, seconds = inputString[:-1].split(' ')
        elif inputString[0] in self.validLongDirections:
            direction = inputString[0]
            degrees, minutes, seconds = inputString[1:].split(' ')
        else:
            raise ValueError
        dMS = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
        if 0 <= dMS <= 180:
            self.degrees = float(degrees)
            self.minutes = float(minutes)
            self.seconds = float(seconds)
            self.compassDirection = direction.upper()
        else:
            raise ValueError


class Item(object):
    def __init__(self, startingOwner, startingName, startingWeight, startingColor):
        self.owner = startingOwner
        self.name = startingName
        self.weight = startingWeight
        self.color = startingColor

    def __str__(self):
        return "The %s %s is owned by: %s and weighs %3.2f" % (self.getColor(), self.getName(), self.getOwner(), self.getWeight())

    def setOwner(self, newOwner):
        self.owner = newOwner

    def getOwner(self):
        return self.owner

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setWeight(self, newWeight):
        self.weight = newWeight

    def getWeight(self):
        return self.weight

    def setColor(self, newColor):
        self.color = newColor

    def getColor(self):
        return self.color


class TravelBag(object):
    def __init__(self, startingCapacity, startingColor, startingName):
        self.capacity = startingCapacity
        self.color = startingColor
        self.weight = 0
        self.name = startingName
        self.owner = ""
        self.contents = []

    def __str__(self):
        return f"The {self.getColor()} {self.getName()} bag belongs to {self.getOwner()}; weighs {self.getWeight():3.2f}"

    def __iter__(self):
        self.nextIterPosition = 0
        return self

    def __next__(self):
        if self.nextIterPosition < len(self.contents):
            self.nextIterPosition += 1
            return self.contents[self.nextIterPosition - 1]
        else:
            raise StopIteration

    def addItem(self, newItem):
        if type(newItem) == Item:
            self.contents.append(newItem)
            self.weight += newItem.weight
        else:
            raise TypeError

    def getItem(self, itemName):
        for position, item in enumerate(self.contents):
            if item.getName() == itemName:
                self.weight -= item.weight
                del self.contents[position]
                return item
        return None

    def setOwner(self, newOwner):
        self.owner = newOwner

    def getOwner(self):
        return self.owner

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setWeight(self, newWeight):
        self.weight = newWeight

    def getWeight(self):
        return self.weight

    def setColor(self, newColor):
        self.color = newColor

    def getColor(self):
        return self.color


class Suitcase(TravelBag):
    def __init__(self, startingCapacity, startingColor, startingName):
        if float(suitcaseMinimunSize) <= float(startingCapacity) <= float(suitcaseMaximumSize):
            super().__init__(startingCapacity, startingColor, startingName)
            self.lockCode = ""
            self.currentLocation = []
            self.currentBaggageTag = ""
        else:
            raise ValueError

    def __str__(self):
        location = self.getCurrentLocation()
        if len(location) == 2:
            return f"{super().__str__()} Lock Code: {self.getLockCode()} Location: {location[0]} {location[1]} LuggageTag: {self.getCurrentBaggageTag()}"
        else:
            return f"{super().__str__()} Lock Code: {self.getLockCode()} Location: None LuggageTag: {self.getCurrentBaggageTag()}"

    def setLockCode(self, newCode):
        self.lockCode = newCode

    def getLockCode(self):
        return self.lockCode

    def setCoordinates(self, latitude, longitude):
        if type(latitude) is Latitude and type(longitude) is Longitude:
            self.currentLocation = [latitude, longitude]
        else:
            raise ValueError

    def getCurrentLocation(self):
        return self.currentLocation

    def setCurrentBaggageTag(self, newTagNumber):
        self.currentBaggageTag = newTagNumber

    def getCurrentBaggageTag(self):
        return self.currentBaggageTag