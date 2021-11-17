def check_line(line):
    oper = line.split()
    summ = 0
    try:
        oper[0], oper[2] = check_num((oper[0], oper[2]))
        check_operation(oper[1])
        summ += execute_operation(oper)
    except ValueError:
        print(f"В строке {line}, некорректные знчения!", end="\t")
        summ += change_oper()
    except SyntaxError:
        print(f"В строке {line}, некорректная операция!", end="\t")
        summ += change_oper()
    except ZeroDivisionError:
        print(f"В строке {line}, деление на 0!", end="\t")
        summ += change_oper()
    finally:
        return summ

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

def change_oper():
    answer = input("Хотите исправить? ")
    if answer.lower() == "да":
        new_line = input("Введите исправленную строку: ")
        return check_line(new_line.replace('\n', ''))
    else:
        return 0

with open("calc.txt", "r") as calc:
    summ = 0
    for line in calc:
        summ += check_line(line.replace('\n', ''))
    print("Сумма всех операций =", summ)




