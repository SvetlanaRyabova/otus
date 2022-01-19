import math


# Треугольник
class Triangle:
    def __init__(self, *sides):
        self.name = "Трегольник"
        self.sides = tuple(sides)
        self._area = None
        self._perimeter = None

    # геттер
    def get_sides(self):
        return self.sides

    # сеттер
    def set_sides(self, value):
        self.sides = value

    # площадь
    @property
    def area(self):
        p = sum(self.sides) / 2
        intermediate_calculation = 1
        for i in range(len(self.sides)):
            intermediate_calculation = (p - self.sides[i]) * intermediate_calculation
        self._area = math.sqrt(p * intermediate_calculation)
        return self._area

    # периметр
    @property
    def perimeter(self):
        self._perimeter = sum(self.sides)
        return self._perimeter


a = Triangle(4, 2, 3)
print(a.area)
print(a.perimeter)
