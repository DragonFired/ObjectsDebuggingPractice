#!/usr/bin/env python
__author__ = "Arana Fireheart"

from person2 import *
from datetime import datetime

person1 = Person(datetime(2017, 11, 9))
person2 = Person(datetime(1927, 1, 1))
person3 = Person(datetime(1982, 1, 1))
person1.speak("Hello")
person1.speak("there")
person1.speak("stranger")
person1.speak("What's new?")
person1.phraseCleanup()
print(person1.getAge())
print(person2.getAge())
print(person3.getAge())
pass