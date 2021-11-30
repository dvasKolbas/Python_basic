import random

class Human:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 30
        self.house = house
        self.happiness = 100

    def eat(self):
        max_food = self.house.get_fridge()
        if max_food > 30:
            max_food = 30
        num = random.randint(1, max_food)
        self.satiety += num
        self.house.use_food(num)

    def pet_the_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def on_sofa(self):
        self.happiness += 30
        self.satiety -= 10

    def check_satiety(self):
        if self.satiety < 10:
            return True
        else:
            return False

    # def check_all(self):
    #     if self.house.check_house() and self.satiety >= 0:
    #         return True
    #     else:
    #         return False

    def check_dirt(self):
        if self.house.get_dirt() >= 90:
            self.happiness -= 10

    def check_happiness(self):
        if self.happiness <= 20:
            return True
        else:
            return False

    def check_dying(self):
        if self.happiness < 10 or self.satiety < 0:
            print(self.name, "умер, ", end="")
            return True
        return False

    def print_result(self):
        print(f"У {self.name}:\n"
              f"Сытость: {self.satiety}\n"
              f"Счастье: {self.happiness}\n")

class Man(Human):
    def play(self):
        self.happiness += 20
        self.satiety -= 10


    def work(self):
        self.satiety -= 10
        self.house.add_salary(150)

    def action(self):
        value = random.randint(1, 6)
        if self.check_satiety() and not self.house.check_fridge():
            self.eat()
        elif self.check_happiness() and not self.check_satiety():
            self.play()
        elif self.house.check_money() and not self.check_satiety():
            self.work()
        elif value == 1 and not self.check_satiety():
            self.work()
        elif value == 2 and not self.house.check_fridge():
            self.eat()
        elif value > 2 and not self.check_satiety():
            self.pet_the_cat()
        else:
            self.on_sofa()
        dying = self.check_dying()
        return dying

class Woman(Human):
    def market(self):
        max_food = 200 - self.house.get_fridge()
        if max_food > 10:
            num_food = random.randint(10, max_food)
            money = self.house.get_money()
            if num_food > money:
                num_food = money
            self.house.add_food(num_food)
            self.house.use_money(num_food)

        max_cat_food = 100 - self.house.get_cat_food()
        if max_cat_food > 10:
            num_cat_food = random.randint(10, max_cat_food)
            money = self.house.get_money()
            if num_cat_food > money:
                num_cat_food = money
            self.house.add_cat_food(num_cat_food)
            self.house.use_money(num_cat_food)


        self.satiety -= 10

    def cleaning(self):
        num = self.house.get_dirt()
        if num > 100:
            num = 100
        self.house.cleaning()
        self.satiety -= 10

    def byu_fur_coat(self):
        self.happiness += 60
        self.house.add_fur_coat()
        self.house.use_money(350)
        self.satiety -= 10

    def action(self):
        value = random.randint(1, 6)
        if self.check_satiety() and not self.house.check_fridge():
            self.eat()
        elif self.house.check_food() and not self.check_satiety():
            self.market()
        elif self.check_happiness() and not self.check_satiety() and self.house.check_fur_coat():
            self.byu_fur_coat()
        elif value == 1 and not self.check_satiety() and self.house.check_fur_coat():
            self.byu_fur_coat()
        elif value == 2 and not self.house.check_fridge():
            self.eat()
        elif value > 2 and not self.check_satiety():
            self.pet_the_cat()
        else:
            self.on_sofa()
        dying = self.check_dying()
        return dying

class Cat():
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.satiety = 30

    def eat(self):
        max_food = self.house.get_cat_food()
        if max_food > 10:
            max_food = 10
        num = random.randint(1, max_food)
        self.satiety += num * 2
        self.house.use_cat_food(num)

    def play(self):
        self.house.add_dirt()
        self.satiety -= 10

    def sleep(self):
        self.satiety -= 10

    def check_satiety(self):
        if self.satiety < 10:
            return True
        else:
            return False

    def dying(self):
        if self.satiety < 0:
            print(self.name, "умер, ", end="")
            return True
        else:
            return False

    def action(self):
        value = random.randint(1, 6)
        if self.check_satiety() and not self.house.check_cat_food():
            self.eat()
        elif (value == 1 or value == 2) and not self.check_satiety():
            self.play()
        elif value == 3 and not self.house.check_cat_food():
            self.eat()
        elif value > 3:
            self.sleep()
        dying = self.dying()
        return dying

    def print_result(self):
        print(f"У {self.name}:\n"
              f"Сытость: {self.satiety}\n")
