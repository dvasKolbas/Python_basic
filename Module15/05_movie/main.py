def create_like(films, count):
    like_films = []
    while count > 0:
        like_film = input("\nВведите любимый фильм: ")
        if check_film(films, like_film):
            like_films.append(like_film)
        else:
            print("Такого фильма в списке нет!")
        count -= 1
    return like_films


def check_film(films, like_film):
    create = False
    for i in films:
        if like_film == i:
            create = True
            break
    return create


films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо",
         "Отступники", "Деревня"]
count = int(input("Введите кол-во фильмов: "))
like_films = create_like(films, count)
print("\nЛюбимые фильмы:", like_films)

