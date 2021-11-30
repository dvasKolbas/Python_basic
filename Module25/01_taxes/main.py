import propety
def tax_pay():
    money = input_value("Введите кол-во денег: ")
    appartment = input_value("Введите стоимость квартиры: ")
    car = input_value("Введите стоимость машины: ")
    country_house = input_value("Введите стоимость дачи: ")
    tax = tax_calculation(appartment, car, country_house)
    check_money(money, tax)

def input_value(text):
    value = 0
    while True:
        try:
            value = int(input(text))
            return value
        except ValueError:
            print("Некорректное значение!")

def tax_calculation(appartment, car, country_house):
    tax = round(propety.Appartment(appartment).get_tax()
    + propety.Car(car).get_tax() \
    + propety.CountryHouse(country_house).get_tax(), 2)
    return tax

def check_money(money, tax):
    if money >= tax:
        print("Олично, денег хватает!")
    else:
        print("Грустно, не хватает ", tax - money, "рублей")

tax_pay()