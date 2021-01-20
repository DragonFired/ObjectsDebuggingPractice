#!/usr/bin/env python
__author__ = "Arana Fireheart"

from person import *

person1 = Person("Mindy")
person1.setHeight(123)
person1.setWeight(133)
person1.speak("Hello")
person1.speak("Good Bye")
person1.speak("What?")
person1.speak("Nothing!")
person1.speak("Why?")
print(person1)
print("---------")
print(person1.pastPhrases())
print("---------")
print(person1.pastPhrases(4))
print("---------")
try:
    print(person1.pastPhrases(-10))
except ValueError:
    print("Usage error: numberOfSteps must be positive.")
print(person1.getGender())
man1 = Man("George")
man1.setHeight(345)
man1.setWeight(220)
print(man1.getGender())
woman1 = Woman("Martha")
woman1.setHeight(345)
woman1.setWeight(220)
print(woman1.getGender())
