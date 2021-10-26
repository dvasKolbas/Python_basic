def countdown(N, K):
    list_humans = list(range(1, N + 1))
    start = 0
    while len(list_humans) > 1:
        print("\nТекущий круг людей:", list_humans)
        if start > len(list_humans) - 1:
            start = 0
        print("Начало счёта с номера", list_humans[start])
        index = ((start + K) % len(list_humans)) -1
        print("Выбывает человек под номером", list_humans[index])
        list_humans.remove(list_humans[index])
        start = index
    print("\nОстался человек под номером", list_humans[0])

N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))

print(f"Значит, выбывает каждый {K} человек")

countdown(N, K)
