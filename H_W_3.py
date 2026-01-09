from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education
    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def age(self):
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
        today = datetime.today()
        age = today.year - birth.year

        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return age

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"У меня {edu_text}."
        )
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Я учился с Бектуром в группе {self.group}. "
            f"У меня {edu_text}."
        )

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Мое хобби {self.hobby}. "
            f"У меня {edu_text}."
        )

cl1 = Classmate("Аян", "15.12.2008", "студент", True, "КС-2-24")
cl1.introduce()

fr1 = Friend("Эмир", "27.10.2007", "школьник", True, "футбол")
fr1.introduce()
print(fr1.age)