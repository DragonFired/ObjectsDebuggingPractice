__author__ = 'Arana Fireheart'

from travelBag import Item, TravelBag, Suitcase, Latitude, Longitude

itemInfo = [['Bob', 'keys', 1.7, 'Sliver'],
            ['Bob', 'wallet', 12.4, 'Brown'],
            ['Patryce', 'phone', 2.02, 'Black'],
            ['Arana', 'iPad', 17.7, 'Slate Grey'],
            ['Jose', 'hat', 3.2, 'Blue']]
objectList = []

for ownerName, itemName, weight, color in itemInfo:
    objectList.append(Item(ownerName, itemName, weight, color))

for parameter in objectList:
    print(parameter)

someItem = objectList[2]
someItem.setName('remote')
someItem.setOwner('No One')
someItem.setWeight(22.4)
someItem.setColor('Red')

print("**** Testing TravelBag object ****")
myTravelBag = TravelBag(3, "Blue", "Backpack")
print(myTravelBag)
myTravelBag.setOwner("Mickey Mouse")
print(myTravelBag.getName())
myTravelBag.setName("LunchBox")
print(myTravelBag.getName())
myTravelBag.setWeight(27.0)
print(myTravelBag.getWeight())
myTravelBag.setWeight(0.0)
print(myTravelBag.getWeight())
myTravelBag.setColor("Green")
print(myTravelBag)

# Fill the bag up with the items previously built.
for item in objectList:
    myTravelBag.addItem(item)

print(myTravelBag)
print(myTravelBag.getItem("iPad"))

print("**** Testing Suitcase object ****")
try:
    brokenSuitcase = Suitcase(1200, "Purple", "Weekender")
except ValueError:
    print("Suitcase too large!")
mySuitcase = Suitcase(12, "Purple", "Weekender")
print(mySuitcase)
mySuitcase.setOwner("Mickey Mouse")
print(mySuitcase.getName())
mySuitcase.setName("Weeklong")
print(mySuitcase.getName())
mySuitcase.setWeight(27.0)
print(mySuitcase.getWeight())
mySuitcase.setWeight(0.0)
print(mySuitcase.getWeight())
mySuitcase.setColor("Blue")
mySuitcase.setLockCode("197832")
print(mySuitcase)
mySuitcase.setCurrentBaggageTag("0B7NF120943")
print(mySuitcase)

myLatitude = Latitude("41 25 01N")
print(myLatitude)
myLongitude = Longitude("120 58 57W")
print(myLongitude)
anotherLatitude = Latitude("S17 33 08.352")
print(anotherLatitude)
anotherLongitude = Longitude("W69 01 29.74")
print(anotherLongitude)
try:
    anotherLatitude = Latitude("S217 33 08.352")
except ValueError:
    print("Value out of range")

try:
    anotherLongitude = Longitude("W269 01 29.74")
except ValueError:
    print("Value out of range")

try:
    anotherLatitude = Latitude("E17 33 08.352")
except ValueError:
    print("Value out of range")

try:
    anotherLongitude = Longitude("N69 01 29.74")
except ValueError:
    print("Value out of range")

mySuitcase.setCoordinates(myLatitude, myLongitude)
print(mySuitcase)
try:
    mySuitcase.setCoordinates("North", myLongitude)
except ValueError:
    print("You need to use valid Latitude and Longitude objects for values")
try:
    mySuitcase.setCoordinates(myLatitude, "South")
except ValueError:
    print("You need to use valid Latitude and Longitude objects for values")
pass