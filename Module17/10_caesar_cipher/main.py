def coding_text(text, a, K):
  new_text = [a[a.index(i) + K - 33] if i != " " else " " for i in text]
  print("".join(new_text))

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
text = input("Введите текст: ")
K = int(input("Введите сдвиг: "))
coding_text(text, alphabet, K)