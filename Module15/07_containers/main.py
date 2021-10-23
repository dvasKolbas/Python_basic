def input_weight(count):
    containers = []
    while count > 0:
        cont = int(input("Введите вес контейнера: "))
        if check_container(cont):
            count -= 1
            containers.append(cont)
    return containers


def check_container(cont):
    if 0 < cont <= 200:
        return True
    else:
        print("Некорректный вес контейнера, введите еще раз!")
        return False


def new_container(containers):
    new_containers = []
    while True:
        cont = int(input("\nВведите вес нового контейнера: "))
        if check_container(cont):
            input_new_cont = False
            for i in range(len(containers)):
                if containers[i] < cont and not (input_new_cont):
                    new_containers.append(cont)
                    input_new_cont = True
                    print("\nНомер, куда встанет новый контейнер:", i + 1)
                new_containers.append(containers[i])
            break


count = int(input("Введите кол-во контейнеров: "))
print()
containers = input_weight(count)
new_container(containers)
