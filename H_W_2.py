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
            return f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.profession}, высшее образование есть"
        elif self.profession != " " and self.higher_education == False:
            return f"меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.profession}, высшего образования нет"
        else:
            return f"Меня зовут {self.name}, я родился {self.birth_date}, профессии нет, высшего образования нет"
class Classmate(Person):
    def __init__(self, name, friend_name, birth_date, higher_education, profession, group_name):
        super().__init__(name, birth_date, higher_education, profession)
        self.group_name = group_name
        self.friend_name = friend_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник {self.friend_name}, я родился {self.birth_date}, я работаю {self.profession}")

class Friend(Person):
    def __init__(self, name, friend_name,  birth_date, higher_education, profession, hobby):
        super().__init__(name, birth_date, higher_education, profession)
        self.hobby = hobby
        self.friend_name = friend_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг {self.friend_name}, я родился {self.birth_date}, я работаю {self.profession}")
print("*" * 35)
friend = Friend("Ариет", "Гульзины", "11.11.2002", "", "строителем", "рисую")
friend.introduce()
print(friend.hobby)
friend = Friend("Белек", "Карины", "12.01.2008", "", "Врачом", "читаю книги")
friend.introduce()
print(friend.hobby)
print("*" * 35)
classmate = Classmate("Бектур", "Кати", "5.12.2000", "", "программистом", "23")
classmate.introduce()
print(f"номер группы: {classmate.group_name}")
classmate = Classmate("Руся", "Екатерины", "14.12.2009", "", "Зубным", "90")
classmate.introduce()
print(f"номер группы: {classmate.group_name}")