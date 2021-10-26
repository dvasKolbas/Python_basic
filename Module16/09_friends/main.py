def create_credit(credits):
    for i in range(1, credits + 1):
        print()
        print(i, "расписка")
        debtor = int(input("Кому: "))
        creditor = int(input("От кого: "))
        summ = int(input("Сколько: "))
        balance[debtor - 1] -= summ
        balance[creditor - 1] += summ

def create_balace(friends):
    for i in range(friends):
        balance.append(0)

def print_balance():
    print("\nБаланс друзей:")
    for i in range(len(balance)):
        print(i + 1, ":", balance[i])

balance = []
friends = int(input("Кол-во друзей: "))
create_balace(friends)
credits = int(input("Долговых расписок: "))
create_credit(credits)
print_balance()