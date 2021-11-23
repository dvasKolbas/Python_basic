from garden import Gardener

name = input("Введите имя садовника: ")
my_gardener = Gardener(name, 5)
while True:
    count = int(input("Сколько картошки вы хотите получить? Не менее "))
    my_gardener.harvest_from_garden(count)