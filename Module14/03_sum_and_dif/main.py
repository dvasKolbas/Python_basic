N = int(input("Введите число: "))
summ = 0
count = 0
for i in str(N):
    summ += int(i)
    count += 1
print("Сумма цифр:", summ)
print("Кол-во цифр в числе:", count)
print("Разность суммы и кол-ва цифр:", summ - count)
