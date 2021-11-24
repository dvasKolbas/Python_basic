from game import Tic_tac_toe

def menu():
    while True:
        print("Играем?\n"
          "1 - Да\n"
          "2 - Нет")
        try:
            play = int(input())
            if play == 1:
                play_game()
            elif play == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Некорректное значение!")


def play_game():
    print("Вы играете крестиками(X)")
    new_game = Tic_tac_toe()
    cont = True
    while cont:
        new_game.print_table()
        try:
            active = int(input("Выберите поле: "))
            if new_game.check_num(active):
                cont = new_game.move(active)
                if cont:
                    cont = new_game.move(0, True)
            else:
                raise ValueError
        except ValueError:
            print("Некорректное значение!")
menu()