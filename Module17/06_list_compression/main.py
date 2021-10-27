import random
def change_list(listt):
  for _ in range(listt.count(0)):
    listt.remove(0)
    listt.append(0)
  return listt

def delete_zero(listt):
  for _ in range(listt.count(0)):
    listt.remove(0)
  return listt

N = int(input("Введите кол-во элементов: "))

list_N = [random.randint(0,2) for _ in range(N)]
print("Начальный список:", list_N)
list_N = change_list(list_N)
print("Нули в конце:", list_N)
list_N = delete_zero(list_N)
print("Без нулей:", list_N)