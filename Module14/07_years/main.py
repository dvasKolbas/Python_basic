def print_year(start_year, stop_year):
    print(f"Года от {start_year} до {stop_year} с тремя одинаковыми цифрами:")
    for i in range(start_year, stop_year):
        if check_year(i):
            print(i)

def check_year(year):
    year_list = list(str(year))
    if year_list.count(year_list[0]) == 3 or year_list.count(year_list[1]) == 3:
        return True
    else:
        return False
    # a = year % 10
    # b = (year // 10) % 10
    # c = (year // 100) % 10
    # d = year // 1000
    # count = 0
    # for i in range(2):
    #     if a == b:
    #        count += 1
    #     if a == c:
    #         count += 1
    #     if a == d:
    #         count += 1
    #     if count == 2:
    #         return True
    #     else:
    #         count = 0
    #         a, b = b, a
    # return False


start_year = int(input("Введите первый год: "))
stop_year = int(input("Введите второй год: "))
print_year(start_year, stop_year)