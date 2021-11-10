
def move(n, x, z, y):
    if n == 1:
        print("Переложить диск 1 со стержня номер {} на стержень номер {}".format(x, y))
        return
    move(n - 1, x, y, z)
    print("Переложить диск {} со стержня номер {} на стержень номер {}".format(n, x, y))
    move(n - 1, z, x, y)

N = int(input("Введите кол-во дисков: "))
move(N, 1, 2, 3)