vowels = "уеаоэяию"
text = input("Введите текст: ")
text_vowels = [l for l in text if vowels.count(l) > 0]
print("Список гласных букв:", text_vowels)
print("\nДлина списка:", len(text_vowels))