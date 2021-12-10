from collections import Counter

def can_be_poly(string: str) -> bool:
    count = Counter(string)
    odd = len(list(filter(lambda x: x % 2 != 0, list(count.values()))))
    if (len(string) % 2 == 0 and odd == 0) or (len(string) % 2 != 0 and odd == 1):
        return True
    else:
        return False

print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))

