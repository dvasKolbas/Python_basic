class House:
    def __init__(self):
        self.__fridge = 50 # 200 максимум еды в холодильнике
        self.__money = 100
        self.__cat_food = 30 # 50 максимум еды у кота
        self.__dirt = 0
        self.__wardrobe = 0
        self.__food_count = 0
        self.__cat_food_count = 0
        self.__money_count = 0

    def add_salary(self, num):
        self.__money += num
        self.__money_count += num

    def add_food(self, num):
        self.__fridge += num

    def add_cat_food(self, num):
        self.__cat_food += num

    def add_fur_coat(self):
        self.__wardrobe += 1

    def add_dirt(self):
        self.__dirt += 5

    def use_food(self, num):
        self.__fridge -= num
        self.__food_count += num

    def use_cat_food(self, num):
        self.__cat_food -= num
        self.__cat_food_count += num

    def use_money(self, num):
        self.__money -= num

    def cleaning(self):
        self.__dirt = 0

    def get_fridge(self):
        return self.__fridge

    def get_cat_food(self):
        return self.__cat_food

    def get_dirt(self):
        return self.__dirt

    def get_money(self):
        return self.__money

    def check_fridge(self):
        if self.__fridge <= 0:
            return True
        else:
            return False

    def check_cat_food(self):
        if self.__cat_food <= 0:
            return True
        else:
            return False

    def check_food(self):
        if self.__fridge <= 100 or self.__cat_food <= 50:
            return True
        else:
            return False

    def check_money(self):
        if self.__money < 50:
            return True
        else:
            return False

    # def check_house(self):
    #     if self.__money >= 0 and self.__fridge >= 0:
    #         return True
    #     else:
    #         return False

    def check_fur_coat(self):
        if self.__money >= 350:
            return True
        else:
            return False

    def print_result(self):
        print(f"Заработали денег: {self.__money_count}\n"
              f"Съели еды: {self.__food_count}\n"
              f"Кот съел еды: {self.__cat_food_count}\n"
              f"Шуб в гардеробе: {self.__wardrobe}")
