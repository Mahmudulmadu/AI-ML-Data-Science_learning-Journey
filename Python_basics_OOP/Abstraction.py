from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar..!!")

class Cow(Animal):
    def make_sound(self):
        print("Hamba")

lion = Lion()
lion.make_sound()