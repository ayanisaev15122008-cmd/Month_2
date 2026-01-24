from abc import ABC, abstractmethod
import math

class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Ошибка: Возраст не может быть отрицательным!")

    def get_age(self):
        return self.__age

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move_vehicle(vehicle):
    print(vehicle.move())

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":
    print("--- Инкапсуляция ---")
    p = Person()
    p.set_age(25)
    print(f"Возраст: {p.get_age()}")
    p.set_age(-5)

    print("\n--- Наследование ---")
    dog = Dog("Buddy")
    cat = Cat("Kitty")
    print(dog.name, dog.speak())
    print(cat.name, cat.speak())

    print("\n--- Полиморфизм ---")
    car = Car()
    bike = Bicycle()
    move_vehicle(car)
    move_vehicle(bike)

    print("\n--- Абстракция ---")
    rect = Rectangle(10, 5)
    circle = Circle(7)
    print(f"Площадь прямоугольника: {rect.area()}")
    print(f"Площадь круга: {circle.area():.2f}")