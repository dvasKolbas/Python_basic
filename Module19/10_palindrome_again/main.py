def check_word(word):
    a = set(word)
    if len(a) == 1:
        print("Можно сделать палиндромом")
    elif len(a) < len(word):
        odd = 0
        for i in a:
            if word.count(i) % 2 != 0:
                odd += 1
        if len(word) % 2 == 0 and odd == 0:
            print("Можно сделать палиндромом")
        elif len(word) % 2 != 0 and odd == 1:
            print("Можно сделать палиндромом")
        else:
            print("Нельзя сделать палиндромом")
    else:
        print("Нельзя сделать палиндромом")

while True:
    word = input("Введите строку: ")
    check_word(word)