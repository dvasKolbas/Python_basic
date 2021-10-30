string = input("Введите текст: ").split()
max_word = ""
for i in string:
  if len(i) > len(max_word):
    max_word = i
print(f"Самое длинное слово - {max_word}, его длина {len(max_word)}")