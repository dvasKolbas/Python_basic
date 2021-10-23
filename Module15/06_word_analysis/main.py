def count_letter(word):
  count = 0
  word_list = list(word)
  for i in range(len(word_list)):
    unique = True
    for j in range(len(word_list)):
      if i != j and word_list[i] == word_list[j]:
        unique = False
        break
    if unique:
      count += 1
  print("Кол-во уникальных букв:", count)

word = input("Введите слово: ")
count_letter(word)