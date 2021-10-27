N = int(input("Введите длину списка: "))
list_N = [1 if i % 2 == 0 else i % 5 for i in range(N)]
print("Результат:", list_N)
