# # Abstraction - Hiding Implementation details and exposing only the essential functionality
#
# abc module - abstract bass class

from abc import ABC, abstractmethod

# Abstract class -

class Animal(ABC):   # abstract class
    @abstractmethod
    def sound(self):
        pass
# Implementing a abstract class
class Main(Animal):

    def sound(self):
        print("This is an ANIMAl")

animal = Main()
# animal.sound()