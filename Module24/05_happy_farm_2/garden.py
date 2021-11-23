class Potato:
    states = {0: "Отсутсвует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, index):
        self.infex = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def new_potato(self):
        self.state = 0

    def is_ripe(self):
        if self.state == 3:
            return True
        else:
            return False

    def print_state(self):
        print("Картошка {} сейчас {}".format(self.infex, Potato.states[self.state]))

class Potato_garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print("\nКартошка прорастает")
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            return False
        else:
            return True

    def new_potatos(self):
        for potato in self.potatoes:
            potato.new_potato()
        return len(self.potatoes)

class Gardener:

    def __init__(self, name, count):
        self.name = name
        self.garden = Potato_garden(count)
        self.harvest = []

    def harvest_from_garden(self, count):
        self.harvest.append(0)
        while self.harvest[-1] < count:
            if self.garden.are_all_ripe():
                self.harvest[-1] += self.garden.new_potatos()
            else:
                self.garden.grow_all()
        self.print_harvest()

    def print_harvest(self):
        print("\nЗа текущий сезон, садовник {} собрал картошки {}шт".format(self.name, self.harvest[-1]))
        print("За все время работы, садовник {} собрал картошки {}шт\n".format(self.name, sum(self.harvest)))


