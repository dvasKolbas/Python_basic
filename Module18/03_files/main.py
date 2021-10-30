def check_start(file):
  start = tuple("@№$%^&*()")
  #for i in start:
  if file.startswith(start):
    print(f"Ошибка, файл не может начинаться с {file[0]}\n")
    return True
  return False

def check_end(file):
  end = tuple([".txt", ".docx"])
  #for i in end:
  if file.endswith(end):
      return False
  print(f"Ошибка, файл должен иметь расширение {end}\n")
  return True

cont = True
while cont:
  file = input("Введите название файла: ")
  cont = check_start(file)
  if not cont:
    cont = check_end(file)

print("Файл назван верно")