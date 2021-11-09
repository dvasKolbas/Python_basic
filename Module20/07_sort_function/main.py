import random


def sort_tuple(tup):
    for i in tup:
        if not(isinstance(i, int)):
            return tup
    else:
        return tuple(sorted(tup))


tup1 = tuple(random.randint(1, 10) for _ in range(10))
print("Оригинальный список с целыми числами:", tup1)
tup2 = tuple(random.randint(1, 10) if i % 2 == 0 else round(random.random() * 10, 2) for i in range(10))
print("Оригинальный список с дробными числами:", tup2)
print("\nСортированый список с целыми числами:", sort_tuple(tup1))
print("Сортированый список с дробными числами:", sort_tuple(tup2))