class House:
    def __init__(self):
        self.fridge = 50
        self.money = 0

    def check_fridge(self):
        if self.fridge < 10:
            return True
        else:
            return False

    def check_money(self):
        if self.money < 50:
            return True
        else:
            return False

    def add_salary(self):
        self.money += 50

    def add_food(self):
        self.fridge += 10

    def use_food(self):
        self.fridge -= 10

    def use_money(self):
        self.money -= 50

    def check_house(self):
        if self.money >= 0 and self.fridge >= 0:
            return True
        else:
            return False
