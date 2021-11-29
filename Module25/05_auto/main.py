import auto

new_bus = auto.Bus(0, 0)
while True:
    new_bus.station()
    angle = int(input("Введите угол перемещения автобуса: "))
    distance = int(input("Введите расстояние перемещения автобуса: "))
    new_bus.change_direction(angle, distance)