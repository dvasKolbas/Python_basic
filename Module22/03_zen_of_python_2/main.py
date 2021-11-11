import os
import re


def count_letters(text, a = "abcdefghijklmnopqrstuvwxyz"):
    count = 0
    for i in text:
        if i in a:
            count += 1
    return count

def count_words(text):
    words = re.split("[-\n, ]+", text)
    return len(words)

def count_line(text):
    return text.count("\n") + 1

def rare_letter(text, a = "abcdefghijklmnopqrstuvwxyz"):
    count = ["", len(text)]
    for letter in a:
        if text.count(letter) < count[1]:
            count = [letter, text.count(letter)]
    return count[0]

file = os.path.abspath(os.path.join("..", "02_zen_of_python", "zen.txt"))
print(file)
zen_file = open(file, "r")
text = zen_file.read()
print("Букв:", count_letters(text))
print("Слов:", count_words(text))
print("Строк:", count_line(text))
print("Редкая буква:", rare_letter(text))
zen_file.close()