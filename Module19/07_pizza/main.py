def create_dict(count):
    orders = {}
    for i in range(count):
        order_list = input(f"{i + 1} заказ: ").split()
        #order_list = l1[i].split()
        if orders.get(order_list[0]) == None:
            orders[order_list[0]] = {order_list[1]: int(order_list[2])}
        elif orders.get(order_list[0], {}).get(order_list[1]) == None:
            orders[order_list[0]][order_list[1]] = int(order_list[2])
        else:
            orders[order_list[0]][order_list[1]] += int(order_list[2])
    print_dict(orders)

def print_dict(orders):
    for client in sorted(orders):
        print(client + ":")
        for order in sorted(orders[client]):
            print("\t" + order +": "+ str(orders[client][order]))

#list1 = ["Иванов Пепперони 1", "Петров Де-Люкс 2", "Иванов Мясная 3", "Иванов Мексиканская 2", "Иванов Пепперони 2", "Петров Интересная 5"]
count = int(input("Введите кол-во заказов: "))
create_dict(count)