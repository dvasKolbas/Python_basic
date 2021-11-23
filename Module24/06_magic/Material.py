class Water:
    name = "Вода"

    def __add__(self, other):
        if isinstance(other, Wind):
            return "Шторм"
        if isinstance(other, Fire):
            return "Пар"
        if isinstance(other, Earth):
            return "Грязь"
        if isinstance(other, Human):
            return "Корабль"

class Wind:
    name = "Ветер"

    def __add__(self, other):
        if isinstance(other, Water):
            return "Шторм"
        if isinstance(other, Fire):
            return "Молния"
        if isinstance(other, Earth):
            return "Пыль"
        if isinstance(other, Human):
            return "Самолет"

class Fire:
    name = "Огонь"

    def __add__(self, other):
        if isinstance(other, Water):
            return "Пар"
        if isinstance(other, Wind):
            return "Молния"
        if isinstance(other, Earth):
            return "Лава"
        if isinstance(other, Human):
            return "Двигатель"

class Earth:
    name = "Земля"

    def __add__(self, other):
        if isinstance(other, Water):
            return "Грязь"
        if isinstance(other, Wind):
            return "Пыль"
        if isinstance(other, Fire):
            return "Лава"
        if isinstance(other, Human):
            return "Нефть"

class Human:
    name = "Человек"

    def __add__(self, other):
        if isinstance(other, Wind):
            return "Самолет"
        if isinstance(other, Fire):
            return "Двигатель"
        if isinstance(other, Earth):
            return "Нефть"
        if isinstance(other, Water):
            return "Корабль"