from collections.abc import Iterable

class Iterator:
    def __init__(self, num: int) -> None:
        self.current = 0
        self.count = num

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> int:
        if self.current < self.count:
            self.current += 1
            return self.current ** 2
        else:
            raise StopIteration

def square(num: int) -> Iterable:
    for i in range(1, num + 1):
        yield i ** 2

N = int(input("Введите число: "))
print("Через класс:")
for num in Iterator(N):
    print(num, end=" ")

print("\nЧерез функцию:")
for num in square(N):
    print(num, end=" ")

print("\nЧерез выражение:")
for num in (i ** 2 for i in range(1, N + 1)):
    print(num, end=" ")



