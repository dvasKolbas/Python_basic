def input_cards(count, cards):
    max_card = 0
    for i in range(count):
        card = int(input(str(i + 1) + " Видеокарта: "))
        if card > max_card:
            max_card = card
        cards.append(card)
    return cards, max_card


def print_cards(cards, max_card):
    print("\nСтарый список видеокарт:", cards)
    new_cards = []
    for i in range(len(cards)):
        if cards[i] != max_card:
            new_cards.append(cards[i])
    print("\nНовый список видеокарт:", new_cards)


count = int(input("Кол-во видеокарт: "))
cards = []
cells, max_card = input_cards(count, cards)
print_cards(cards, max_card)