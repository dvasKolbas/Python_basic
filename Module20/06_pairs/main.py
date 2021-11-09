import random

original_list = [random.randint(0, 9) for i in range(10)]
print("Оригинальный список:", original_list)
new_list = [(original_list[i], original_list[i+1])for i in range(0, len(original_list), 2)]
print(new_list)
new_list2 = list(zip(original_list[0:10:2], original_list[1:10:2]))
print(new_list2)