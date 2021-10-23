def create_list(N):
    odd_num = []
    for i in range(1, N + 1, 2):
        odd_num.append(i)
    print(odd_num)


N = int(input("Введите число: "))
create_list(N)