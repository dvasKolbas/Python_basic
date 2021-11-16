import random


def create_exception_list(i):
    exception_list = [ValueError, ZeroDivisionError, FileNotFoundError, TabError, TypeError, ArithmeticError]
    raise exception_list[i]

summ = 0
try:
    with open("value.txt", "a") as file_value:
        while summ < 777:
            value = int(input("Введите число: "))
            summ += value
            if random.randint(1, 13) == 13:
                create_exception_list(random.randint(0, 5))
            file_value.write(str(value))
        print("Сумма чисел больше или равна 777")
except:
    print("Ошибка, программа завершена!")
