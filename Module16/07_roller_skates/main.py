def create_skates(count):
    list_skates = []
    for i in range(count):
        list_skates.append(int(input("Размер " + str(i + 1) + " пары: ")))
    return list_skates

def create_humans(count):
    list_humans = []
    for i in range(count):
        list_humans.append(int(input("Размер ноги " + str(i + 1) + " человека: ")))
    return list_humans

def check_count(humans, skates):
    max_humans = 0
    for i in humans:
        check_humans = min(humans.count(i), skates.count(i))
        max_humans += check_humans
        for _ in range(0, check_humans):
            skates.remove(i)
    print("\nНаибольшее кол-во людей, которые могут взять ролики: ", max_humans)

skates = create_skates(int(input("Кол-во коньков: ")))
humans = create_humans(int(input("\nКол-во людей: ")))
check_count(humans, skates)