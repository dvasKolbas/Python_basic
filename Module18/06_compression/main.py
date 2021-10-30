string = input("Введите строку: ")
new_string = ""
a = string[0]
count = 1
for i in range(1, len(string)):
    if string[i] != a:
        new_string += a + str(count)
        a = string[i]
        count = 1
    else:
        count += 1
    if i == len(string) - 1:
        new_string += a + str(count)
print(new_string)
