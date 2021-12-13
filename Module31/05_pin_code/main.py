import itertools

nums = [i for i in range(10)]
pincode = tuple(int(i) for i in input("Введите пин-код: "))
for pin in itertools.permutations(nums, 4):
    if pincode == pin:
        print("Ваш пин-код:", pin)
        break

