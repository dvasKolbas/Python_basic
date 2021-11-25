class Fighter:
        health = 100
        damage = 20

        def __init__(self, num):
            self.name = "Воин" + str(num)

        def defend(self):
            self.health = self.health - self.damage

        def is_lose(self):
            if self.health <= 0:
                return True

        def attack(self, defender):
            defender.defend()

