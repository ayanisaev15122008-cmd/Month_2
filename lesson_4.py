
from abc import ABC, abstractmethod

# абстрактный
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def test(self):
        pass
# конкретный
class Dog(Animal):
    def test(self):
        print("test")
    def make_sound(self):
        print("Гав гав")

class Cat(Animal):
    def test(self):
        print("test")
    def make_sound(self):
        print("Мяу мяу")

puppy = Dog()
puppy.make_sound()
kitty = Cat()
kitty.make_sound()