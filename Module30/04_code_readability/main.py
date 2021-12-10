def siple_value():
    value = list()
    for i in range(1000):
        count = 0
        for n in range(1, i + 1):
            if i % n == 0:
                count += 1
        if count == 2:
            value.append(i)
    return value

print(siple_value())

print([i for i in range(1000) if len(list(n for n in range(1, i + 1) if i % n == 0)) == 2])
print([i for i in range(1000) if not len(list(n for n in range(2, i) if i % n == 0))])
