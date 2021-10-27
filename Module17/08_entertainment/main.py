import random

def throw(list_N, count):
  start = random.randint(0, 9)
  stop = random.randint(start, 9)
  print(f"Бросок {count}. Сбиты палки с номера {start + 1} по номер {stop + 1}")
  for i in range(start, stop + 1):
    list_N[i] = "."
  count += 1
  return list_N, count


N = int(input("Введите кол-во палочек: "))
K = int(input("Введите кол-во бросков: "))
list_N = ["|" for _ in range(N)]
count = 1
while count <= K:
  list_N, count = throw(list_N, count)
print("Результат:", "".join(list_N))