import os.path

def find_dir(dir_list, path = os.path.abspath("/")):
    for dir in dir_list:
        if not (dir in os.listdir(path)):
            return None
        path = os.path.join(path, dir)
    return path

text = input("Введите строку: ")
dir = input("Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n").split()
print()
path = find_dir(dir)
if path:
    file_name = input("Введите имя файла: ") + ".txt"
    file_path = os.path.join(path, file_name)
    if find_dir([file_name], path):
        answer = input("Вы действительно хотите перезаписать файл? ")
        if answer.title() == "Да":
            file = open(file_path, "w")
            file.write(text)
            file.close()
            print("Файл успешно перезаписан!")
        else:
            print("Файл не изменен!")
    else:
        file = open(file_path, "w")
        file.write(text)
        file.close()
        print("Файл успешно сохранён!")
else:
    print("Такого пути не существует!")