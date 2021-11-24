import random


class Blackjack:
    cards = {"Двойка": 2,
            "Тройка": 3,
            "Четверка": 4,
            "Пятерка": 5,
            "Шестерка": 6,
            "Семерка": 7,
            "Восьмерка": 8,
            "Девятка": 9,
            "Десятка": 10,
            "Валет": 10,
            "Дама": 10,
            "Кароль": 10,
            "Туз": 11,
            }

    def __init__(self):
        self.cards_lst = [key for key in self.cards.keys()]
        self.player_cards = []
        self.dealer_cards = []
        self.start()

    def start(self):
        for _ in range(2):
            self.give_card()
            self.give_card(True)
        self.print_cards()


    def give_card(self, comp = False):
        player = self.player_cards
        if comp:
            player = self.dealer_cards
        player_card = random.choice(self.cards_lst)
        player.append(player_card)
        self.cards_lst.remove(player_card)

    def check_point(self, player):
        points = 0
        for card in player:
            if card == "Туз" and points >= 21:
                points += 1
            else:
                points += self.cards[card]
        return points


    def stop(self):
        return self.print_cards(True)

    def winner(self, dealer, player):
        if dealer == player:
            print("Ничья!")
        elif dealer < player:
            print("Вы выиграли!")
        else:
            print("Дилер выиграл!")
        print()

    def print_cards(self, comp = False):
        player = self.check_point(self.player_cards)
        if player > 21:
            print("У Вас", player, "очков, больше чем необходимо!\n"
                                   "Ваши карты:", ", ".join(self.player_cards))
            self.winner(player + 1, player)
            return False
        else:
            print("У Вас", player, "очков\n"
                                      "Ваши карты:", ", ".join(self.player_cards))
            if comp:
                dealer = self.check_point(self.dealer_cards)
                print("У диллера", dealer, "очков\n"
                                           "Карты диллера:", " ,".join(self.dealer_cards))

                self.winner(dealer, player)
                return False
            return True
