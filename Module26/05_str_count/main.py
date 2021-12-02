import os

def find_file():
    print(os.getcwd())
    for elem in os.listdir(os.getcwd()):
        if elem.endswith(".py"):
            yield sum([i for i in line_count(elem)])

def line_count(file_name):
    with open(file_name, "r") as file:
        for line in file.readlines():
            if line != "\n" and not line.startswith("#"):
                yield 1

print(sum([i for i in find_file()]))


