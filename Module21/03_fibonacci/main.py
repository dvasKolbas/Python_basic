def fib(n, list_fib):
  if len(list_fib) != n:
    list_fib.append(sum(list_fib[len(list_fib)-2:len(list_fib)]))
    fib(n, list_fib)

n = int(input("Введите позицию числа в ряде Фибоначчи: "))
list_fib = [1]
fib(n, list_fib)
print("Число:", list_fib[n - 1])