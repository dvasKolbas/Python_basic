from blackjack import Blackjack

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
    new_game = Blackjack()
    cont = True
    while cont:
        print("Ваше действие?\n"
              "1 - Взять карту\n"
              "2 - Остановиться")
        try:
            active = int(input())
            if active == 1:
                new_game.give_card()
                cont = new_game.print_cards()
            elif active == 2:
                cont = new_game.stop()
            else:
                raise ValueError
        except ValueError:
            print("Некорректное значение!")
menu()