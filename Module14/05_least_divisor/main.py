def find_divider(N):
    res = 0
    for i in range(2, N+1):
        if N % i == 0:
            res = i
            return i

N = int(input("Введите число: "))
d = find_divider(N)
print("Наименьший делитель, отличный от единицы:", d)
