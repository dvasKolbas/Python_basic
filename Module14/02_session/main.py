# TODO здесь писать код
print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = 0
while True:
    x2 = float(input('X: '))
    if x2 == x1:
        print("Координата X двух точек не может быть равна!")
    else:
        break
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
k = y_diff / x_diff
b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)