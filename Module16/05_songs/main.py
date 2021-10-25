def choice(num, duration):
    song = input(f"Название {num} песни: ")
    index = find_song(song)
    if index == -1:
        print("Такой песни в списке нет!")
    else:
        duration += violator_songs[index][1]
        num += 1
    return num, duration

def find_song(song):
    for i in range(len(violator_songs)):
        if violator_songs[i][0] == song:
            return i
    return -1
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
count = int(input("Сколько песен выбрать? "))
num = 1
duration = 0
while num <= count:
    num, duration = choice(num, duration)

print(f"\nОбщее время звучания песен: {round(duration, 2)} минут")
