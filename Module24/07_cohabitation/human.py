import random

class Human:


    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        self.satiety += 20
        self.house.use_food()

    def work(self):
        self.satiety -= 20
        self.house.add_salary()

    def market(self):
        self.house.add_food()
        self.house.use_money()

    def play(self):
        self.satiety -= 20

    def check_satiety(self):
        if self.satiety < 20:
            return True
        else:
            return False

    def check_all(self):
        if self.house.check_house() and self.satiety >= 0:
            return True
        else:
            return False

    def action(self):
        brk = False
        value = random.randint(1, 6)
        if self.check_satiety() and not self.house.check_fridge():
            self.eat()
        elif self.house.check_fridge() and not self.house.check_money():
            self.market()
        elif self.house.check_money() and not self.check_satiety():
            self.work()
        elif value == 1 and not self.check_satiety():
            self.work()
        elif value == 2 and not self.house.check_fridge():
            self.eat()
        elif value > 2 and not self.check_satiety():
            self.play()
        else:
            print(self.name, "умер,", end="")
            brk = True
        return brk

