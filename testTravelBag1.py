__author__ = "Arana Fireheart"

from shoulderbag import *
from random import randint

itemsNames = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eigth', 'ninth', 'tenth']
itemsList = []
for number in range(0, len(itemsNames) - 1, 2):
    itemsList.append(Item(number, 'Me', itemsNames[number], randint(10, 100)/10))
    itemsList.append(Item(number + 1, 'You', itemsNames[number + 1], randint(10, 100)/10))

print("testing Item methods")
itemsList[7].setOwner("Us")
eigthtsWeight = itemsList[7].getWeight()
itemsList[7].setWeight(42)
print(itemsList[7])
itemsList[7].setWeight(eigthtsWeight)
print(itemsList[7])
itemsList[7].setColor("Blue")
print(itemsList[7])
itemsList[7].setName("EIGTH")
print(itemsList[7])
print(itemsList[7].getStoredItem())
itemsList[7].setStoredItem(27)
print(itemsList[7].getStoredItem())

print("Test Item Compare")
if itemsList[7] == itemsList[8]:
    print("Items do match")
else:
    print("Items don't match")
if itemsList[7] == itemsList[7]:
    print("Items do match")

print("Testing ShoulderBag methods")
firstBag = ShoulderBag(8)

print(firstBag)
firstBag.setName("DayPack")
firstBag.setOwner("Arana")
firstBag.setColor("Red")
firstBag.setCapacity(10)

print("\nAdding to Bag")
if firstBag.isEmpty():
    for item in itemsList:
        firstBag.addItem(item)
        # print(firstBag)
print("There are %i items in your bag" % firstBag.howManyItems())
print(firstBag)
print("\nTest overloading")
try:
    firstBag.addItem(itemsList[0])
except:
    print("Failed to overload the bag")

print("\nTest check & retreive")
print(firstBag.checkItem(itemsList[2]))
print(firstBag.retreiveItem('third'))
print(firstBag.checkItem(itemsList[2]))
print(firstBag.retreiveItem('twelfth'))
print("\nEmptying Bag")
while not firstBag.isEmpty():
    print(firstBag.retreiveLastItem())
print("There are %i items in your bag" % firstBag.howManyItems())

print("\nRefilling Bag")
if firstBag.isEmpty():
    for item in itemsList:
        firstBag.addItem(item)
        # print(firstBag)
print("There are %i items in your bag" % firstBag.howManyItems())
print(firstBag)
print("Test emptying bag")
print(firstBag.retreiveLastItem())
print(firstBag.retreiveLastItem())
firstBag.emptyBag()
print(firstBag)
pass