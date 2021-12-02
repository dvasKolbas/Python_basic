import os

def find_dir(file, desired_dir, current_dir):
    for elem in os.listdir(current_dir):
        path = os.path.join(current_dir, elem)
        if elem == desired_dir:
            return
        elif os.path.isdir(path):
            for file_path in find_dir(file, desired_dir, path):
                file.write(file_path + "\n") #Почему функция не переносит сама строку?
        elif os.path.isfile(path):
            yield path

def delete_file():
    if "files.txt" in os.listdir(os.getcwd()):
        os.remove(os.path.abspath(os.path.join("files.txt")))

delete_file()
with open("files.txt", "a") as file:
    start_dir = os.path.abspath(os.path.join("..", "..", ".."))
    desired_dir = input("Введите нужную папку: ")
    for file_path in find_dir(file, desired_dir, start_dir):
        file.write(file_path)