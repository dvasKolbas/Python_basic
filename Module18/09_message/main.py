def change_word(word):
  abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
  new_word = ""
  start = 0
  stop = 0
  for i in range(len(word)):
    if word[i].lower() in abc:
        start = i
        if i == 0:
            stop = (len(word) + 1) * -1
    else:
        new_word += word[start:stop:-1] + word[i]
        start = i
        stop = i
  new_word += word[start:stop:-1]
  return new_word

msg = input("Введите сообщение: ").split()
print(msg)
for j in range(len(msg)):
  msg[j] = change_word(msg[j])

print(" ".join(msg))