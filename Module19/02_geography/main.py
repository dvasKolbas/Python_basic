count_country = int(input("Введите кол-во стран: "))
country = dict()
print("Введите страну и города по шаблону через пробел(Страна Город1 Город2 Город3 и тд)")
for i in range(count_country):
    country_list = input(f"{i + 1} страна: ").split()
    for j in range(1, len(country_list)):
        country[country_list[j]] = country_list[0]
print()
for city_num in range(3):
    city = input(f"{city_num + 1} город: ")
    get_country = country.get(city)
    if get_country != None:
        print(f"Город {city} расположен в стране {get_country}.\n")
    else:
        print(f"По городу {city} данных нет.\n")

