from parents import Parent

def read_file():
    parents = []
    with open("text.txt") as file:
        for line in file:
            line_list = line.split()
            if line_list[0] == "p":
                parents.append(Parent(line_list[1], int(line_list[2])))
            else:
                parents[-1].create_child(line_list[0])
    return parents

def print_parents(parents):
    for parent in parents:
        parent.print_info()

def print_parents_short(parents):
    for id, parent in enumerate(parents):
        print(id + 1, end=") ")
        parent.print_short()

def main_menu(parents):
    while True:
        print_parents_short(parents)
        print("\nВыберите действией:"
              "\nВыберите родителя для действия!"
              "\n0 - Вывести родителей и детей на экран")
        choice = int(input(""))
        if choice == 0:
            print_parents(parents)
        elif 0 < choice <= len(parents):
            deep_menu(parents[choice - 1])
        else:
            print("Некорректная команда!")

def deep_menu(parent):
    print("Выберите действией:"
          "\n1 - Накормить всех детей"
          "\n2 - Успокоить всех детей"
          "\n0 - Вернуться в главное меню")
    choice = int(input())
    if choice == 1:
        parent.feed()
        parent.print_info()
    elif choice == 2:
        parent.calm_down()
        parent.print_info()
    elif choice != 0:
        print("Некорректная команда!")

parents = read_file()
main_menu(parents)