def Boris(value):
    while True:
        answer_b = input("Нужное число есть среди вот этих чисел: ")
        if answer_b == "Помогите!":
            print("Артём мог загадать следующие числа:", *value)
            break
        else:
            b_value = set([int(i) for i in answer_b.split()])
            value = Artem(b_value, value)
            if len(value) == 1:
                print("Ответ", *value)
                break

def Artem(b_value, value):
    answer_a = input("Ответ Артёма: ")
    if answer_a == "Да":
        return value.intersection(b_value)
    else:
        return value.difference(b_value)

max_value = int(input("Введите максимальное число: "))
value = {i for i in range(1, max_value + 1)}
Boris(value)
