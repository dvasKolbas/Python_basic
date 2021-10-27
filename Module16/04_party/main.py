def menu():
    night = False
    answer = input("Гость пришел или ушел? ")
    if answer == "пришел":
        create_guest()
    elif answer == "ушел":
        delete_guest()
    elif answer == "Пора спать":
        night = True
        print("\nВечеринка закончилась, все легли спать.")
    else:
        print("Неизвестная команда!")
    return night

def create_guest():
    name = input("Имя гостя: ")
    if len(guests) > 5:
        print(f"Прости, {name}, но мест нет.")
    else:
        guests.append(name)
        print(f"Привет, {name}!")

def delete_guest():
    name = input("Имя гостя: ")
    if guests.count(name) == 0:
        print("Такого гостя нет на вечеринке!")
    else:
        guests.remove(name)
        print(f"Пока, {name}!")

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
night = False
while not(night):
    print(f"\nСейчас на вечеринке {len(guests)} человек: ", guests)
    night = menu()

