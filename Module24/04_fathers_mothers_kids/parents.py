from children import Children
import random
class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def print_short(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Детей: {len(self.children)}")

    def print_info(self):
        print(f"\nИмя: {self.name}, Возраст: {self.age}, Дети:")
        for child in self.children:
            child.print_child()

    def calm_down(self):
        for child in self.children:
            child.calm_down()

    def feed(self):
        for child in self.children:
            child.feed()

    def create_child(self, name):
        self.children.append(Children(name, random.randint(1, self.age - 16),
                                      random.choice([True, False]),
                                      random.choice([True, False])))