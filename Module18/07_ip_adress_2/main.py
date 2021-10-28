def check_count(ip):
  if len(ip) != 4:
    return True
  return False

def check_value(ip):
  num = "1234567890"
  for value in ip:
    for i in value:
      if num.count(i) == 0:
        return True
  return False

def check_int(ip):
  for i in ip:
    if not (0 <= int(i) <= 255):
      return True
  return False

cont = True
while cont:
  ip_adress = input("Введите IP: ").split(".")
  if check_count(ip_adress):
    print("Мало значений")
  elif check_value(ip_adress):
    print("Значения содержат буквы, символы, или являются не целыми!")
  elif check_int(ip_adress):
    print("Значения больше допустимых(от 0 до 255)")
  else:
    print("IP-адрес корректен")
    cont = False