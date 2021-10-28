text = input("Введите текст: ").split()
text_list = [[i[j] if j != 0 else i[j].upper() for j in range(len(i))] for i in text]
text_list = ["".join(i) for i in text_list]
print(" ".join(text_list))