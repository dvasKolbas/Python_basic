def sequence(n: list):
    if n == [1, 1]:
        for _ in range(10):
            Q = n[-n[-1]] + n[-n[-2]]
            n.append(Q)
            yield Q
    else:
        return

print([i for i in sequence([1, 1])])



