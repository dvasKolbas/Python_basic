import os
import zipfile

def extract_zip():
    zipfile.ZipFile("voyna-i-mir.zip").extractall()

def read_text():
    file = open("voyna-i-mir.txt", "r")
    text = file.read()
    file.close()
    os.remove(os.path.join("voyna-i-mir.txt"))
    return count_letter(text)

def count_letter(text, a = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"):
    a += a.upper()
    count = {letter: text.count(letter) for letter in a if text.count(letter) > 0}
    return sort_letter(count)

def sort_letter(count):
    count_sort = sorted(count.items(), key=sort_count, reverse=True)
    string = "\n".join(i[0] + " " + str(i[1]) for i in count_sort)
    return string

def sort_count(k):
    return k[1]

extract_zip()
new_file = open("analysis.txt", "w")
new_file.write(read_text())
new_file.close()