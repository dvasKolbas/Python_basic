def check_num(values):
    if not (values[0].isnumeric() and values[1].isnumeric()):
        raise ValueError
    return int(values[0]), int(values[1])

def check_operation(oper):
    operation_tuple = ("+", "-", "/", "//", "%", "*", "**")
    if not oper in operation_tuple:
        raise SyntaxError

def execute_operation(oper):
    value = 0
    if oper[2] == 0 and oper[1] in ("/", "//", "%"):
        raise ZeroDivisionError
    elif oper[1] == "+":
        value = oper[0] + oper[2]
    elif oper[1] == "-":
        value = oper[0] - oper[2]
    elif oper[1] == "*":
        value = oper[0] * oper[2]
    elif oper[1] == "**":
        value = oper[0] ** oper[2]
    elif oper[1] == "/":
        value = oper[0] / oper[2]
    elif oper[1] == "//":
        value = oper[0] // oper[2]
    elif oper[1] == "%":
        value = oper[0] % oper[2]
    return value

with open("calc.txt", "r") as calc:
    summ = 0
    for num, line in enumerate(calc):
        oper = line.split()
        try:
            oper[0], oper[2] = check_num((oper[0], oper[2]))
            check_operation(oper[1])
            summ += execute_operation(oper)
        except ValueError:
            print(f"В строке {num + 1}, некорректные знчения!")
        except SyntaxError:
            print(f"В строке {num + 1}, некорректная операция!")
        except ZeroDivisionError:
            print(f"В строке {num + 1}, деление на 0!")
    print("Сумма всех операций =", summ)




