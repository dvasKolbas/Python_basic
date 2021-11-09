site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def print_site(site, string = "", space = 0):
    if string == "":
        string = "site = {{"
        space = len(string)
        string += "\n"
    for i_key, i_value in site.items():
        if isinstance(i_value, dict):
            temp_string = " " * space + i_key
            string += temp_string + ": {{\n"
            string = print_site(i_value, string, len(temp_string))
        else:
            value = i_value
            if i_key == "title":
                value = 'Куплю/продам {brend} недорого'
            elif i_key == "h2":
                value = 'У нас самая низкая цена на {brend}'
            string += " " * space + "'" + i_key + "': '" + value + "'\n"
    string += " " * (space - 1) + "}}\n"
    return string

count = int(input("Сколько сайтов: "))
site_str = print_site(site)
site_list = []
for i in range(count):
    name = input("Введите название продукта для нового сайта: ")
    site_list.append(site_str.format(brend = name))
    print("\n".join(site_list))
