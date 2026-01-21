class Distance:
    units = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        if unit not in self.units:
            raise ValueError("Неизвестная единица измерения")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self.units[self.unit]

    def __add__(self, other):
        total_meters = self.to_meters() + other.to_meters()
        new_value = total_meters / self.units[self.unit]
        return Distance(new_value, self.unit)

    def __sub__(self, other):
        result_meters = self.to_meters() - other.to_meters()
        if result_meters < 0:
            raise ValueError("Результат не может быть отрицательным")
        new_value = result_meters / self.units[self.unit]
        return Distance(new_value, self.unit)

    def __eq__(self, other):
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        return self.to_meters() >= other.to_meters()

d1 = Distance(7, "m")
d2 = Distance(3, "km")
d3 = Distance(1999, "cm")

print(d1)
print(d2)
print(d3)

print(d1 + d2)
print(d2 - d1)

print(d1 == d3)
print(d1 < d2)