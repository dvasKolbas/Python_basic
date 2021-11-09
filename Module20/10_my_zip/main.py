def zip_func(f_block, s_block):
    f_block = list(f_block)
    s_block = list(s_block)
    a = ((f_block[i], s_block[i]) for i in range(min(len(f_block), len(s_block))))
    print(a)
    for i in a:
        print(i)
    print()

string = "abcd"
tup = (10, 20, 30, 40)
zip_func(string, tup)

string = {1:2, 3:4, 5:6}
tup = (10, 20, 30, 40)
zip_func(string, tup)
