import os

def find_file():
    print("Введите путь для сканирования:")
    path = input()
    # for elem in os.listdir(os.getcwd()):
    for elem in os.listdir(path):
        if elem.endswith(".py"):
            yield sum([i for i in line_count(elem)])

def line_count(file_name):
    with open(file_name, "r") as file:
        for line in file.readlines():
            if line != "\n" and not line.startswith("#"):
                yield 1

print(sum([i for i in find_file()]))


