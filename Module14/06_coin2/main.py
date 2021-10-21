import math

def check_coin(a, b, r):
    c = math.sqrt(a**2 + b**2)
    if c <= r:
        return True
    else:
        return False

print("Введите координаты монетки:")
x = float(input("X: "))
y = float(input("Y: "))
r = int(input("Введите радиус: "))
coin = check_coin(abs(x), abs(y), r)

if coin:
    print("\nМонетка где-то рядом")
else:
    print("\nМонетки в области нет")
