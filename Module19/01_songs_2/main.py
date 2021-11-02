def choice(num, duration, v_songs):
    song = input(f"Название {num} песни: ")
    if not(song in v_songs):
        print("Такой песни в списке нет!")
    else:
        duration += v_songs[song]
        num += 1
    return num, duration

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
count = int(input("Сколько песен выбрать? "))
num = 1
duration = 0
while num <= count:
    num, duration = choice(num, duration, violator_songs)
print(f"\nОбщее время звучания песен: {round(duration, 2)} минут")
