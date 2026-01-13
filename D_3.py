import math
from operator import getitem


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        self.area = self.side * self.side
        return self.area

    def diagonal(self):
        self.diagonal = f"{self.side * math.sqrt(2):.2f}"
        return self.diagonal


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
