def create_skates(count):
    list_skates = []
    max_size = 0
    for i in range(count):
        size = int(input("Размер " + str(i + 1) + " пары: "))
        if size > max_size:
            max_size = size
        list_skates.append(size)
    return list_skates, max_size

def create_humans(count):
    list_humans = []
    for i in range(count):
        list_humans.append(int(input("Размер ноги " + str(i + 1) + " человека: ")))
    return list_humans

def check_count(humans, skates, max_size):
    max_humans = 0
    for i in humans:
        if skates.count(i) > 0:
            max_humans += 1
            skates.remove(i)
        else:
            for j in range(i + 1, max_size + 1):
                if skates.count(j) > 0:
                    max_humans += 1
                    skates.remove(j)
    #     check_humans = min(humans.count(i), skates.count(i))
    #     max_humans += check_humans
    #     for _ in range(0, check_humans):
    #         skates.remove(i)
    print("\nНаибольшее кол-во людей, которые могут взять ролики: ", max_humans)

skates, max_size = create_skates(int(input("Кол-во коньков: ")))
humans = create_humans(int(input("\nКол-во людей: ")))
check_count(humans, skates, max_size)