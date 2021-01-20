__author__ = 'Arana Fireheart'

from shoulderBag2 import Item

itemInfo = [['Bob', 'keys', 1.7, 'Sliver'],
            ['Bob', 'wallet', 12.4, 'Brown'],
            ['Patryce', 'phone', 202, 'Black'],
            ['Arana', 'iPad', 407.7, 'Slate Grey'],
            ['Jose', 'hat', 3.2, 'Blue']]
objectList = []

for parameter in itemInfo:
    objectList.append(Item(parameter[0], parameter[1], parameter[2], parameter[3]))

for parameter in objectList:
    print(parameter)

someItem = objectList[2]
someItem.setName('remote')
someItem.setOwner('No One')
someItem.setWeight(22.4)
someItem.setColor('Red')

pass