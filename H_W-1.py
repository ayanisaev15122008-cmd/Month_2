class Person:
    def __init__(self, name, birth_date, higher_education, profession = " "):
        self.name = name
        self.birth_date = birth_date
        self.higher_education = higher_education
        self.profession = profession
        if higher_education == "нет":
            self.higher_education = False
        if higher_education == "да":
            self.higher_education = True
    def introduce(self):
        if self.profession == " " and self.higher_education == True:
            return f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.profession}, высшее образование есть"
        elif self.profession != " " and self.higher_education == True:
            return  f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.profession}, высшее образование есть"
        elif self.profession != " " and self.higher_education == False:
            return f"меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.profession}, высшего образования нет"
        else:
            return f"Меня зовут {self.name}, я родился {self.birth_date}, профессии нет, высшего образования нет"


Person_1 = Person("Ратмир", "19.01.2009", "да", "лингвист")
Person_2 = Person("Аян", "15.12.2008", "нет")
Person_3 = Person("Айя", "23.03.2035", "нет", "психолог")
print(Person_1.name)
print(Person_1.birth_date)
print(Person_1.higher_education)
print(Person_1.introduce())
print("#" * 35)
print(Person_2.name)
print(Person_2.birth_date)
print(Person_2.higher_education)
print(Person_2.introduce())
print("#" * 35)
print(Person_3.name)
print(Person_3.birth_date)
print(Person_3.higher_education)
print(Person_3.introduce())