nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def one_list(lst, new_list = []):
    for i in lst:
        if isinstance(i, list):
            new_list = one_list(i, new_list)
        else:
            new_list.append(i)
    return new_list

print("Ответ:", one_list(nice_list))