# Прямоугольник
class Rectangle:
    def __init__(self, *sides):
        self.name = "Прямоугольник"
        self.sides = tuple(sides)
        self._area = None
        self._perimeter = None

    # геттер
    def get_side(self):
        return self.sides

    # сеттер
    def set_side(self, value):
        self.sides = value
        # raise ValueError('The side should be positive number')

    # площадь
    @property
    def area(self):
        self._area = self.sides[0] * self.sides[1]
        return self._area

    # периметр
    @property
    def perimeter(self):
        self._perimeter = self.sides[0] + self.sides[1]
        return self._perimeter


a = Rectangle(1, 2)
print(a.area)
print(a.perimeter)
