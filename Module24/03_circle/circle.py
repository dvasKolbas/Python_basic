import math
class Circle:

    def __init__(self, num, center, radius):
        self.num = num
        self.center = center
        self.radius = radius

    def square(self):
        return round(math.pi * (self.radius ** 2), 2)

    def perimeter(self):
        return round(math.pi * self.radius * 2, 2)

    def increase(self, k):
        self.radius *= k

    def print(self):
        print(self.num, "   ", self.center, "   ", self.radius,
              "  ", self.square(), " ", self.perimeter())


class Circle_list:

    def __init__(self):
        self.cicles = []
        with open("circle.txt", "r") as circle_file:
            for id, line in enumerate(circle_file):
                new_circle = line.split()
                self.cicles.append(Circle(int(id + 1), (int(new_circle[0]), int(new_circle[1])), int(new_circle[2])))

    def print_circles(self):
        print()
        print("Номер", " Центр ", "Радиус", "Площадь", "Периметр")
        for circle in self.cicles:
            circle.print()

    def increase_circles(self, k):
        for circle in self.cicles:
            circle.increase(k)
        self.print_circles()

    def check_intersections(self):
        print()
        for i, circle_1 in enumerate(self.cicles):
            for j in range(i + 1, len(self.cicles)):
                circle_2 = self.cicles[j]
                if circle_1.center == circle_2.center:
                    print(f"Окружность {i + 1} пересекается с окружностью {j + 1}")
                else:
                    legs = tuple(circle_1.center[i] - circle_2.center[i] for i in range(2))
                    hypotenuse = math.sqrt(legs[0]**2 + legs[1]**2)
                    if hypotenuse <= circle_1.radius + circle_2.radius:
                        print(f"Окружность {i + 1} пересекается с окружностью {j + 1}")



