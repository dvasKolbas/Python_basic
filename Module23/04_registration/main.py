def check_count(user):
    if len(user) != 3:
        raise IndexError

def check_name(name):
    if not name.isalpha():
        raise NameError

def check_email(email):
    if not('@' in email and '.' in email):
        raise SyntaxError

def check_age(age):
    if age.isnumeric():
        if 10 <= int(age) <= 99:
            return
    raise ValueError

def create_log(file, user):
        file.write(" ".join(user) + "\n")

with open("registrations.txt", "r") as registration:
    with open("registrations_bad.log", "a") as file_bad:
        with open("registrations_bad.log", "a") as file_good:
            for num, line in enumerate(registration):
                user = line.split()
                file = file_good
                try:
                    check_count(user)
                    check_name(user[0])
                    check_email(user[1])
                    check_age(user[2])
                except IndexError:
                    print(f"В строке {num + 1}, некорректное количество полей!")
                    user.append("IndexError")
                    file = file_bad
                except NameError:
                    print(f"В строке {num + 1}, некорректное имя!")
                    user.append("NameError")
                    file = file_bad
                except SyntaxError:
                    print(f"В строке {num + 1}, некорректный email!")
                    user.append("SyntaxError")
                    file = file_bad
                except ValueError:
                    print(f"В строке {num + 1}, некорректный возраст!")
                    user.append("ValueError")
                    file = file_bad
                finally:
                    create_log(file, user)