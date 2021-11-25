class Water:
    name = "Вода"

    def __add__(self, other):
        if isinstance(other, Wind):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Dirt()
        if isinstance(other, Human):
            return Ship()

class Wind:
    name = "Ветер"

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        if isinstance(other, Human):
            return Airplane()

class Fire:
    name = "Огонь"

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Wind):
            return Lightning()
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Human):
            return Engine()

class Earth:
    name = "Земля"

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Wind):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Human):
            return Oil()

class Human:
    name = "Человек"

    def __add__(self, other):
        if isinstance(other, Wind):
            return Airplane()
        if isinstance(other, Fire):
            return Engine()
        if isinstance(other, Earth):
            return Oil()
        if isinstance(other, Water):
            return Ship()

class Storm():
    def __str__(self):
        return "Шторм"

class Steam():
    def __str__(self):
        return "Пар"

class Dirt():
    def __str__(self):
        return "Грязь"

class Ship():
    def __str__(self):
        return "Корабль"

class Lightning():
    def __str__(self):
        return "Молния"

class Dust():
    def __str__(self):
        return "Пыль"

class Airplane():
    def __str__(self):
        return "Самолет"

class Lava():
    def __str__(self):
        return "Лава"

class Engine():
    def __str__(self):
        return "Двигатель"

class Oil():
    def __str__(self):
        return "Нефть"