word = input("Введите слово: ")
list_word = list(word)
first_part = ""
second_part = ""
for i in range(len(list_word) // 2):
  first_part += list_word[i]
  second_part = list_word[i] + second_part
if len(list_word) % 2 != 0:
  first_part += list_word[len(list_word) // 2] + second_part
else:
  first_part += second_part
if first_part == word:
  print("Слово является палиндромом")
else:
  print("Слово не является палиндромом")
