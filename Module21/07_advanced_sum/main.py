def summ_f(*args):
    lst = list(args)
    summ = 0
    for i in lst:
        if isinstance(i, list):
            summ += summ_f(i)
        else:
            summ += i
    return summ

res = summ_f(1, 2, 3, 4, 5)
print("Ответ:", res)