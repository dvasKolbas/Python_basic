def check_letter(text):
    letter = set(text)
    count = {}
    for i in letter:
        count[text.count(i)] = count.get(text.count(i), "") + i

    return count

text = input("Введите текст: ")
print(check_letter(text))