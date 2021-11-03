import random

def is_prime(n):
    if n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    return True

def create_lst():
    lst = [random.randint(1, 10) for _ in range(10)]
    print(lst)
    new_lst = [i_value for i_index, i_value in enumerate(lst) if is_prime(i_index)]
    return new_lst

def main_f():
    return create_lst()

print(main_f())