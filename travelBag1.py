__author__ = "Arana Fireheart"

class Item(object):
    def __init__(self, startingStoredItem, startingOwner, startingName, startingWeight=0, startingColor='black'):
        self.storedItem = startingStoredItem
        self.owner = startingOwner
        self.name = startingName
        self.weight = startingWeight
        self.color = startingColor

    def __str__(self):
        return "Name: %s, Owner: %s, Weight: %2.5f, Color: %s" %(self.getName(), self.getOwner(), self.getWeight(), self.getColor())

    def __eq__(self, other):
        return self.storedItem == other.storedItem

    def setStoredItem(self, newStoredItem):
        self.storedItem = newStoredItem

    def getStoredItem(self):
        return self.storedItem

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
    def __init__(self, startingCapacity):
        self.capacity = startingCapacity
        self.color = 'black'
        self.weight = 0
        self.name = ''
        self.owner = ''
        self.contents = []

    def __str__(self):
        itemsString = ''
        for item in self.contents:
            itemsString += str(item) + '\n'
        return "Bag Name: %s, Owner: %s, Capacity: %i, Weight: %f, Color %s\n%s" % (self.getName(), self.getOwner(), self.getCapacity(), self.getWeight(), self.getColor(), itemsString)

    def setCapacity(self, newCapacity):
        self.capacity = newCapacity

    def getCapacity(self):
        return self.capacity

    def setColor(self, newColor):
        self.color = newColor

    def getColor(self):
        return self.color

    # def setWeight(self, newWeight):
    #     self.weight = newWeight
    #
    def getWeight(self):
        return self.weight

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setOwner(self, newOwner):
        self.owner = newOwner

    def getOwner(self):
        return self.owner

    def addItem(self, newItem):
        if not self.isFull():
            self.contents.append(newItem)
            self.weight += newItem.getWeight()
        else:
            raise IndexError

    def retreiveItem(self, itemName):
        for postition, item in enumerate(self.contents):
            if item.getName() == itemName:
                del self.contents[postition]
                return item
        return None

    def retreiveLastItem(self):
        self.weight -= self.contents[-1].getWeight()
        return self.contents.pop()

    def checkItem(self, itemObject):
        return itemObject in self.contents


    def emptyBag(self):
        self.contents = []
        self.weight = 0

    def isFull(self):
        return len(self.contents) == self.capacity

    def isEmpty(self):
        return len(self.contents) == 0

    def howManyItems(self):
        return len(self.contents)