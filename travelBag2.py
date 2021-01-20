__author__ = 'Arana Fireheart'

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
        return "The %s %s bag belongs to %s; weighs %3.2f" % (self.getColor(), self.getName(), self.getOwner(), self.getWeight())

    def setContents(self, newContent):
        if type(newContent) == Item:
            self.contents.append(newContent)
        else:
            raise TypeError

    def getContents(self, itemName):
        for item in self.contents:
            if item.getName == itemName:
                return item
        return None