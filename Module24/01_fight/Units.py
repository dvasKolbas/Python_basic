from Figther import Fighter
import random
class Units:
    def __init__(self, count):
        self.fighters = [Fighter(i + 1) for i in range(count)]

    def fight(self):
        attack = random.randint(0, 1)
        defend = attack - 1
        self.fighters[attack].attack(self.fighters[defend])
        #self.fighters[defend].defend()
        self.print(attack, defend)

    def print(self, attack, defend):
        print("{fighter1} наности урон по {fighter2}, "
              "у {fighter2} осталось {health} здоровья".format(
            fighter1= self.fighters[attack].name, fighter2= self.fighters[defend].name,
            health= self.fighters[defend].health
        ))

    def check_health(self):
        for id, figther in enumerate(self.fighters):
            if figther.is_lose():
                self.print_winner(self.fighters[id - 1])
                return False
        else:
            return True

    def print_winner(self, fighter):
        print("\nПобедил {0}".format(fighter.name))
