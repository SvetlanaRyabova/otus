# Круг
class Circle:
    def __init__(self, side):
        self.name = "Круг"
        self.side = side
        self._area = None
        self._perimeter = None

    # геттер
    def get_side(self):
        return self.sides

    # сеттер
    def set_side(self, value):
        self.side = value
        # raise ValueError('The side should be positive number')

    # площадь
    @property
    def area(self):
        self._area = 3.1415 * (self.side ** 2)
        return self._area

    # периметр
    @property
    def perimeter(self):
        self._perimeter = 2 * 3.1415 * self.side
        return self._perimeter


a = Circle(3)
print(a.area)
print(a.perimeter)
