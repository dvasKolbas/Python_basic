def input_number(count):
    value = ""
    for i in range(count):
        value += input("Число: ")
    return value

def check_value(value):
    list_check = list(value)
    first_part = ""
    second_part = ""
    for i in range(len(list_check) // 2):
        first_part += list_check[i]
        second_part = list_check[i] + second_part
    if len(list_check) % 2 != 0:
        first_part += list_check[len(list_check) // 2] + second_part
    else:
        first_part += second_part
    if first_part == value:
        return True
    else:
        return False

def create_symmetry(value):
    if check_value(value):
        print("Последовательность уже симметричная")
        return
    new_value = ""
    count = 0
    for i in value:
        count += 1
        new_value = i + new_value
        if check_value(value + new_value):
            print("Последовательность", " ".join(list(value)))
            print("Нужно приписать чисел:", count)
            print("Сами числа:", " ".join(list(new_value)))
            return

count = int(input("Кол-во чисел: "))
value = input_number(count)
create_symmetry(value)

