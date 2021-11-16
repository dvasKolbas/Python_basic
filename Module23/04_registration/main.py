def chek_count(user):
    if len(user) != 3:
        raise IndexError

def chek_name(name):
    if not name.isalpha():
        raise NameError

def chek_email(email):
    if not('@' in email and '.' in email):
        raise SyntaxError

def chek_age(age):
    if age.isnumeric():
        if 10 <= int(age) <= 99:
            return
    raise ValueError

def create_log(file, user):
    with open(file, "a") as file:
        file.write(" ".join(user) + "\n")

with open("registrations.txt", "r") as registration:
    for num, line in enumerate(registration):
        user = line.split()
        file = "registrations_good.log"
        try:
            chek_count(user)
            chek_name(user[0])
            chek_email(user[1])
            chek_age(user[2])
        except IndexError:
            print(f"В строке {num + 1}, некорректное количество полей!")
            user.append("IndexError")
            file = "registrations_bad.log"
        except NameError:
            print(f"В строке {num + 1}, некорректное имя!")
            user.append("NameError")
            file = "registrations_bad.log"
        except SyntaxError:
            print(f"В строке {num + 1}, некорректный email!")
            user.append("SyntaxError")
            file = "registrations_bad.log"
        except ValueError:
            print(f"В строке {num + 1}, некорректный возраст!")
            user.append("ValueError")
            file = "registrations_bad.log"
        finally:
            create_log(file, user)