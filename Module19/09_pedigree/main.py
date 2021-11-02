def create_height(name, p, h):
    if not(name in h):
        if not(p in h):
            h[name] = 0
        else:
            h[name] = h[p] + 1
    return h

def print_dict(h):
    for i in sorted(h):
        print(i + " " + str(h[i]))


#temp_list = ["Alexei Peter_I", "Anna Peter_I", "Elizabeth Peter_I", "Peter_II Alexei", "Peter_III Anna", "Paul_I Peter_III", "Alexander_I Paul_I", "Nicholaus_I Paul_I"]

#trees = {}
height = {}
count = int(input("Введите количество человек: "))
#count = len(temp_list)
for i in range(count):
    order_list = input(f"{i + 1} пара: ").split()
    #order_list = temp_list[i].split()
    height = create_height(order_list[1], "", height)
    height = create_height(order_list[0], order_list[1], height)
print_dict(height)