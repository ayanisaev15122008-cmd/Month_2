class Animal:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  def get_name(self):
    return self.__name
  def get_age(self):
    return self.__age


  def set_name(self, name):
    self.__name = name
  def set_age(self, age):
    if age >= 0:
      self.__age = age
    else:
      print("возраст не может быть отрицательным")

  def male_sound(self):
      print('Животное издает звуки')

class Dog(Animal):
  def make_sound(self):
    print("Собака издает гав")

class Cat(Animal):
  def male_sound(self):
    print("Кошка издает мяу")

dog = Dog("Барбос", 4)
cat = Cat("Миса", 1)

dog.make_sound()
cat.make_sounr()

dog.set_name("Бобрито")
dog.set_age(5)

cat.set_name("Бурито")
cat.set_age(2)

print(dog.get_name(), dog.get_age())
print(cat.get_name(), cat.get_age())