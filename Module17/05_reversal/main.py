string = input("Введите строку(h - обязательно 2шт): ")
index_start = string.index("h")
index_end = string.index('h', index_start + 1)
new_string = string[index_end - 1:index_start:-1]
print("Найденый текст:", new_string)