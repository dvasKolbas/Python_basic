def create_list(count):
    list_num = []
    for i in range(count):
        list_num.append(int(input("Введите " + str(i + 1) + " число: ")))
    return list_num

def clear_list():
    for i in first_list:
        count_i = first_list.count(i)
        for j in range(1, count_i):
            first_list.remove(i)

print("Введите 3 числа первого списка:")
first_list = create_list(3)
print("Первый список:", first_list)
print("Введите 7 чисел второго списка:")
second_list = create_list(7)
print("Второй список:", second_list)

first_list.extend(second_list)
clear_list()
print("\nНовый первый список с уникальными элементами:", first_list)