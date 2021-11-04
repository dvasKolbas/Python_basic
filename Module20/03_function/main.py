import random

def main_f(tpl, n):
    inpt = False
    start = -1
    stop = len(tpl)
    if tpl.count(n) == 0:
        return tuple()
    for i_index, i_value in enumerate(tpl):
        if i_value == n and start == -1:
            start = i_index
        elif i_value == n and start != -1:
            stop = i_index + 1
            break
    new_tpl = tpl[start:stop]
    return new_tpl

tpl = tuple(random.randint(1,5) for _ in range(10))
n = random.randint(1,5)
print("Начальный кортеж:", tpl)
print("Случайный элемент:", n)
print("Новый кортеж:", main_f(tpl, n))