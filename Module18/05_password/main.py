def check_upper(p, num):
  for i in p:
    if i.upper() == i and num.count(i) == 0 :
      return False
  return True

def check_num(p, num):
  count_num = 0
  for i in num:
    if p.count(i) > 0:
      count_num += p.count(i)
      if count_num >= 3:
        return False
  return True

def check_lenth(p):
  if len(p) >= 7:
    return False
  return True

cont = True
num = "1234567890"
while cont:
  password = input("Введите пароль: ")
  if check_lenth(password):
    print("Длина пароля не меньше семи символов!")
  elif check_num(password, num):
    print("Пароль должен содержать не менее трех цифр!")
  elif check_upper(password, num):
    print("Пароль должен содержать не менее одной заглавной буквы!")
  else:
    cont = False
    print("Пароль принят!")
