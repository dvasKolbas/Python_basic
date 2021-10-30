def coding_text(text, a, a_Up, K):
  new_text = [a[a.index(i) + K - 26] if i in a else (a_Up[a_Up.index(i) + K - 26] if i in a_Up else i) for i in text]
  print("".join(new_text))

def shift_text(word):
    lst = [word[i] for i in range(-1, len(word) - 1)]
    return "".join(lst)

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = input("Введите текст: ").split()
count = 3
for j in range(len(text)):
    for _ in range(count):
        text[j] = shift_text(text[j])
    if "/" in text[j]:
        count += 1
coding_text(" ".join(text), alphabet, alphabet_UP, -1)