def shift(lst):
  lst = [lst[i] for i in range(-1, len(lst)-1)]
  return lst

string1 = input("Первая строка: ")
string2 = list(input("Вторая строка: "))
for i in range(len(string2)):
  if "".join(string2) == string1:
    print(f"Первая строка получается из второй со сдвигом {i}")
    break
  string2 = shift(string2)
else:
  print("Первую строку нельзя получить из второй с помощью циклического сдвига.")