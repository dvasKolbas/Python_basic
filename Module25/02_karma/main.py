import os
from karma import MyKarma

if "karma.log" in os.listdir():
    os.remove(os.path.join("karma.log"))

with open("karma.log", "a") as file:
    my_karma = MyKarma(file)
    count_day = 0
    while True:
        count_day += 1
        try:
            if my_karma.one_day():
                break
        except:
            pass
    print("Вы достигли просвещения за ", count_day, "дней")
