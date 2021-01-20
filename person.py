__author__ = "Arana Fireheart"
from datetime import datetime

class Person(object):

    def __init__(self, startingName):
        self.name = startingName
        self.dateOfBirth = datetime.date(datetime.now())
        self.age = datetime.date(datetime.now()) - self.dateOfBirth
        self.height = 0
        self.weight = 0
        self.eyeColor = None
        self.phrases = []
        self.gender = None

    def __str__(self):
        return "Name: {0} Height:  {1} Weight: {2} Age: {3} Number of past phrases: {4}".format(self.name, self.height, self.weight, self.age, len(self.phrases))

    def speak(self, phraseToSpeak):
        self.phrases.append(phraseToSpeak)
        print(phraseToSpeak)

    def pastPhrases(self, numberOfSteps = 1):
        if numberOfSteps > 0:
            return self.phrases[-numberOfSteps:]
        else:
            raise ValueError

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setDateOfBirth(self, newDate):
        self.dateOfBirth = newDate

    def getDateOfBirth(self):
        return self.dateOfBirth

    def getAge(self):
        return self.age

    def setHeight(self, newHeight):
        self.height = newHeight

    def getHeight(self):
        return self.height

    def setWeight(self, newWeight):
        self.weight = newWeight

    def getWeight(self):
        return self.weight

    def setEyeColor(self, newEyeColor):
        self.eyeColor = newEyeColor

    def getEyeColor(self):
        return self.eyeColor

    def getGender(self):
        return self.gender


class Man(Person):

    def __init__(self, startingName):
        super().__init__(startingName)
        self.gender = "Male"

class Woman(Person):

    def __init__(self, startingName):
        super().__init__(startingName)
        self.gender = "Female"

