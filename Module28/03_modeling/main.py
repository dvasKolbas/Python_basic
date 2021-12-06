import math

class Figure:
    def __init__(self, parties):
        self.__parties = parties

    @property
    def sqr(self):
        sqr = 0
        for i in self.__parties:
            sqr += self.__parties[i].sqr
        return sqr


class Cube(Figure):
    def __init__(self, parties):
        self.__parties = [Square(parties) for _ in range(6)]
        super().__init__(self.__parties)

    # @property
    # def sqr(self):
    #     return self.__parties.sqr * 6

    # @property
    # def parties(self):
    #     return self.__parties

    # @parties.setter
    # def parties(self, Square):
    #     self.__parties = Square

class Square:
    def __init__(self, length):
        self.__parties = length

    @property
    def sqr(self):
        return self.__parties ** 2

    @property
    def perimeter(self):
        return self.__parties * 4

    @property
    def parties(self):
        return self.__parties

    @parties.setter
    def parties(self, length):
        self.__parties = length

class Pyramid(Figure):
    def __init__(self, base, height):
        self.__parties = [Treangle(base, height) for _ in range(4)]
        self.__parties.append(Square(base))
        super().__init__(self.__parties)

    # @property
    # def sqr(self):
    #     base = Square(self.__parties.base)
    #     return self.__parties.sqr * 4 + base.sqr
    #
    # @property
    # def parties(self):
    #     return self.__parties
    #
    # @parties.setter
    # def parties(self, Treangle):
    #     self.__parties = Treangle

class Treangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height
        self.__p()

    @property
    def sqr(self):
        return (self.__base * self.__height / 2)

    @property
    def perimeter(self):
        return (self.__base + self.__parties * 2)

    def __p(self):
        self.__parties = math.sqrt((self.__base / 2) ** 2 + self.__height ** 2)

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base):
        self.__base = base

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__parties = height

my_square = Square(5)
print("Периметр квадрата, со стороной 5:", my_square.perimeter)
my_cube = Cube(5)
print("Площадь куба:", my_cube.sqr)
my_treangle = Treangle(3, 5)
print("Периметр треугольника, со основанием 3 и высотой 5:", round(my_treangle.perimeter, 1))
my_pyramid = Pyramid(3, 5)
print("Площадь пирамиды:", my_pyramid.sqr)
