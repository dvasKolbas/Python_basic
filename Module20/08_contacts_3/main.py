phone_book = {
    ("Иванова", "Алена"): 12345678,
    ("Сидоров", "Иван"): 12345679,
    ("Петров", "Миша"): 12345670
}

def menu(phone_book):
    while True:
        print("Выберите действие:"
              "\n1 - добавить контакт"
              "\n2 - поиск в контактах")
        answer = int(input())
        if answer == 1:
            phone_book = create_contact(phone_book)
        elif answer == 2:
            name = input("Введите фамилию человека: ").title()
            find_contact(phone_book, name)
        else:
            print("Вы ввели некорректную команду!"
                  "\nПопробуйте еще раз.")

def create_contact(phone_book):
    name = tuple(input("Введите фамилию и имя человека через пробел(Фамилия Имя): ").title().split())
    if name in phone_book.keys():
            print("Контакт с такими данными уже есть в книге!")
    else:
        num = int(input("Введите номер: "))
        phone_book[name] = num
        print_pb(phone_book)
    return phone_book

def find_contact(phone_book, name):
    for i_key, i_value in phone_book.items():
        if name in i_key:
            print(*i_key, i_value)
            print()

def print_pb(phone_book):
    for i_key, i_value in phone_book.items():
        print(*i_key, i_value)
        print()

menu(phone_book)