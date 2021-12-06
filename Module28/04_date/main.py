import math


class Cube:
    def __init__(self, Square):
        self.parties = Square

    def sqr(self):
        return self.parties.sqr * 6

    @property
    def parties(self):
        return self.parties

    @parties.setter
    def parties(self, Square):
        self.parties = Square

class Square:
    def __init__(self, length):
        self.__parties = length

    def sqr(self):
        return self.__parties ** 2

    def perimeter(self):
        return self.__parties * 4

    @property
    def parties(self):
        return self.__parties

    @parties.setter
    def parties(self, length):
        self.__parties = length

class Pyramid:
    def __init__(self, Treangle):
        self.parties = Treangle

    def sqr(self):
        base = Square(self.parties.base)
        return self.parties.sqr * 4 + base.sqr

    @property
    def parties(self):
        return self.parties

    @parties.setter
    def parties(self, Treangle):
        self.parties = Treangle

class Treangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.__p()

    def sqr(self):
        return (self.base * self.height / 2)

    def perimeter(self):
        return (self.base + self.__parties * 2)

    def __p(self):
        self.__parties = math.sqrt((self.base / 2) ** 2 + self.height ** 2)

    @property
    def base(self):
        return self.base

    @base.setter
    def base(self, base):
        self.base = base

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self.parties = height

my_square = Square(5)
print("Периметр квадрата, со стороной 5:", my_square.perimeter)
# my_cube = Cube(my_square)
# print("Площадь куба:", my_cube.sqr)
# my_treangle = Treangle(3, 5)
# print("Периметр треугольника, со основанием 3 и высотой 5:", my_treangle.perimeter)
# my_pyramid = Pyramid(my_treangle)
# print("Площадь пирамиды:", my_pyramid.sqr)
