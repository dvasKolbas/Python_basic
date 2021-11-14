length = 0

with open("people.txt", "r") as people:
    for id, line in enumerate(people):
        string = "".join(i for i in line if i.isalpha())
        try:
            if len(string) < 3:
                raise BaseException
            length += len(string)
        except BaseException:
            print(f"Длина строки {id}, меньше 3х символов")
print("Длина символов:", length)
