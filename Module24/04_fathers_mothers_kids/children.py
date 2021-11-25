class Children:
    def __init__(self, name, age, condition, hangry):
        self.name = name
        self.age = age
        self.condition = condition
        self.hangry = hangry

    def feed(self):
        if self.hangry:
            self.hangry = False
        else:
            self.condition = False

    def calm_down(self):
        self.condition = True

    def print_child(self):
        print(f"\tИмя: {self.name}, возраст: {self.age}, спокойный: {self.condition}, голодный: {self.hangry}".replace("True", "Да").replace("False", "Нет"))