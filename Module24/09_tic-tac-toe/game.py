import random


class Tic_tac_toe:

    def __init__(self):
        self.field = [i for i in range(1, 10)]
        self.first_player = "X"
        self.comp = "O"

    def win(self, winner):
        self.print_table()
        print(winner)

    def check(self):
        win_combination = [(0, 1, 2), (0, 4, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (2, 4, 6), (3, 4, 5), (6, 7, 8)]
        for comb in win_combination:
            if self.field[comb[0]] == self.field[comb[1]] == self.field[comb[2]]:
                return True
        else:
            return False

    def check_num(self, num):
        if self.field.count(num) > 0:
            return True
        return False

    def move(self, num, comp= False):
        sym = self.first_player
        winner = "Игрок победил!"
        if comp:
            new_list = [i for i in self.field if isinstance(i, int)]
            if len(new_list) == 0:
                self.win("Ничья!")
                return False
            num = random.choice(new_list)
            sym = self.comp
            winner = "Компьютер победил!"
        self.field[num-1] = sym
        if self.check():
            self.win(winner)
            return False
        return True

    def print_table(self):
        for i in range(0, len(self.field), 3):
            string = f" {self.field[i]} | {self.field[i + 1]} | {self.field[i + 2]}"
            if i != 0:
                print("-" * len(string))
            print(string)
        print()




