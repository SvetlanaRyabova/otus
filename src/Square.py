# Квадрат
class Square:
    def __init__(self, side):
        self.name = "Квадрат"
        self.side = side
        self._area = None
        self._perimeter = None

    # геттер
    def get_side(self):
        return self.side

    # сеттер
    def set_side(self, value):
        self.side = value
        # raise ValueError('The side should be positive number')

    # площадь
    @property
    def area(self):
        self._area = self.side ** 2
        return self._area

    # периметр
    @property
    def perimeter(self):
        self._perimeter = self.side * 4
        return self._perimeter


a = Square(10)
print(a)
print(a.area)
print(a.perimeter)
a.side = 4
print(a.area)
print(a.perimeter)
a.side = -1
print(a.side)

