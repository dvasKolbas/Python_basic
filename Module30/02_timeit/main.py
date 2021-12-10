import timeit

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

print(res)

res_lc: float = timeit.timeit('"-".join(list(str(n) for n in range(100)))', number=10000)

print(res_lc)

res_map: float = timeit.timeit('"-".join(map(str,(n for n in range(100))))', number=10000)

print(res_map)