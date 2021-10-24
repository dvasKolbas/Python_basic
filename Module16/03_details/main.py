shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

while True:
        detail = input("Название детали: ")
        count = int(input("Кол-во деталей: "))
        num = 0
        summ = 0
        for i in range(len(shop)):
                if shop[i][0] == detail:
                        summ += shop[i][1]
                        num += 1
        print("Общая стоимость: ", count * summ/num)