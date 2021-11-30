import tenants
from house import House

new_house = House()
first_human = tenants.Man("Алекс", new_house)
second_human = tenants.Woman("София", new_house)
cat = tenants.Cat("Кошка", new_house)

day = int(input("Введите кол-во дней: "))
for i in range(1, day + 1):
    if first_human.action() or second_human.action() or cat.action():
        print(f"на {i} день")
        break
    new_house.add_dirt()

    # if not first_human.check_all() or not second_human.check_all():
    #     print(f"закончились ресурсы на {i} день")
    #     break
else:
    print(f"Мы прожили {day} дней\n")
first_human.print_result()
second_human.print_result()
cat.print_result()
new_house.print_result()
