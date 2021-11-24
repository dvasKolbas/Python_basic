from human import Human

first_human = Human("Алекс")
second_human = Human("София")

day = int(input("Введите кол-во дней: "))
for i in range(1, day + 1):
    if first_human.action() or second_human.action():
        print(f"на {i} день")
        break

    if not first_human.check_all() or not second_human.check_all():
        print(f"закончились ресурсы на {i} день")
        break
else:
    print(f"Мы прожили {day} дней")
