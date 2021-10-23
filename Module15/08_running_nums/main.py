string = list(input("Введите список: "))
K = int(input("Введите сдвиг: "))

while True:
  for k in range(K):
    for i in range(1, len(string)):
      string[i - 1], string[i] = string[i], string[i - 1]
  print(" ".join(string))
  input("Нажмите любую кнопку!")
