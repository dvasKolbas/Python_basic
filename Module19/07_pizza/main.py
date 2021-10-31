def create_dict(count):
    orders = {}
    for i in range(count):
        order_list = input(f"{i + 1} заказ: ").split()
        orders[order_list[0]] = {order_list[1]: order_list[2]}
    print(orders)

create_dict(6)