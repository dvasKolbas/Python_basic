def main():
    user = input("Введите имя: ")
    while True:
        try:
            action = menu()
            if action == '1':
                print_chat()
            elif action == '2':
                enter_message(user)
            else:
                raise ValueError
        except ValueError:
            print("Некорректное значение!")
        except FileNotFoundError:
            print("Файл chat.txt не найден!")
        except OSError:
            print("Ошибка!")
        except KeyboardInterrupt:
            print("Выход!")
            break

def menu():
    print("Выберите действие: \n"
          "1 - Посмотреть текущий текст чата\n"
          "2 - Отправить сообщение")
    return input()

def print_chat():
    with open("chat.txt", "r") as chat:
        for line in chat:
            message = line.split(" : ", 1)
            print(message[0] + ' : ' + message[1], end = "")
        print()

def enter_message(user):
    with open("chat.txt", "a") as chat:
        print("Введите сообщение:")
        chat.write(user +" : "+ input() + "\n")

main()