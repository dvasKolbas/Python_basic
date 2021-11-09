import random

surname_f = ["Иванова", "Петрова", "Сидорова", "Алехина", "Миронова"]
name_f = ["Маша", "Саша", "Даша", "Аня", "Яна"]

surname_m = ["Иванов", "Петров", "Сидоров", "Алехин", "Миронов"]
name_m = ["Вася", "Петя", "Миша", "Гриша", "Андрей"]

name_ch = ["Дима", "Гоша", "Леша", "Даня", "Денис"]

family = {(surname_m[i], name_m[random.randint(0,4)]):random.randint(30,50) for i in range(5)}
family.update({(surname_f[i], name_f[random.randint(0,4)]):random.randint(30,50) for i in range(5)})
family.update({(surname_m[i], name_ch[random.randint(0,4)]):random.randint(1,10) for i in range(5)})
print(family)

surname = input("Введите фамилию: ").title()
find_surname = (surname, surname + "а", surname[:len(surname)-1])

for i_key, i_value in family.items():
    if i_key[0] in find_surname:
        print(*i_key, i_value)





