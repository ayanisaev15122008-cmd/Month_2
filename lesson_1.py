class Car:
    def __init__(self, model, color):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print(f"Car {self.model} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color

car_subaru = Car("subaru", "red")
car_t = Car("Toyota", "black")
car_n = Car("Nissan", "white")
car_m = Car("Mazda", "pink")
print(car_subaru)
print(car_subaru.model, car_subaru.color)
print(car_t.model, car_t.color)
print(car_n.model, car_n.color)
print(car_m.model, car_m.color)
print(type(car_subaru))
car_subaru.drive_to("Karakol")
car_subaru.change_color("blue")
print(car_subaru.color)
