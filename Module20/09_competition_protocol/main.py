def create_protocol(n):
    # temp = [[69485, "Jack"], [95715, "qwerty"], [95715, "Alex"], [83647, "M"],
    #         [197128, "qwerty"], [95715, "Jack"], [93289, "Alex"], [95715, "Alex"], [95715, "M"]]
    protocol = {}
    print("Записи (результат и имя):")
    for i in range(n):
        data = input(f"{i + 1} запись: ").split()
        #data = temp[i]
        protocol[data[1]] = int(data[0])
    print_winer(protocol)

def print_winer(protocol):
    sort_value = sorted(protocol.values(), reverse=True)[:3]
    print("\nИтоги соревнований:")
    for i in range(3):
        for p_key, p_value in protocol.items():
            if sort_value[i] == p_value:
                print(f"{i + 1} место. {p_key} ({p_value})")
                protocol.pop(p_key)
                break

n = int(input("Сколько записей вносится в протокол? "))
create_protocol(n)