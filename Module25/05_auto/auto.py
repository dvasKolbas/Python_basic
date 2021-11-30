import math


class Automobile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def change_direction(self, angle, distance):
        angle_radians = math.radians(angle)
        self.x += (round(math.cos(angle_radians), 2) * distance)
        self.y += (round(math.sin(angle_radians), 2) * distance)
        self.print_new_coordinates()

    def print_new_coordinates(self):
        print(f"Автомобиль переместился в точку({self.x} , {self.y})")

class Bus(Automobile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.money = 0
        self.passengers = 0

    def change_direction(self, angle, distance):
        super().change_direction(angle, distance)
        self.money += distance * self.passengers

    def station(self):
        self.print_info()
        while True:
            try:
                passengers = self.change_passengers()
                # self.money = 1 * self.passengers
                self.passengers += passengers
                break
            except ValueError:
                print("Некорректное значение пассажиров!")
        self.print_info()

    def change_passengers(self):
        passengers_exit = int(input("Сколько пассажиров вышло: "))
        if passengers_exit > self.passengers:
            raise ValueError
        passengers_enter = int(input("Сколько пассажиров вошло: "))
        return passengers_enter - passengers_exit

    def print_info(self):
        print(f"В автобусе {self.passengers} пассажиров и {self.money} денег")

    def print_new_coordinates(self):
        print(f"Автобус переместился в точку({self.x} , {self.y})")