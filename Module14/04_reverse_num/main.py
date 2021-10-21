def change_num(value):
    change = True
    a = b = ""
    for i in value:
        if i == ".":
            change = False
        else:
            if change:
                a = i + a
            else:
                b = i + b
    return float(a + "." + b)

N = float(input("Введите первое число: "))
new_N = change_num(str(N))
K = float(input("Введите второе число: "))
new_K = change_num(str(K))

print("\nПервое число наоборот:", new_N)
print("Второе число наоборот:", new_K)
print("Сумма:", new_N + new_K)




