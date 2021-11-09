site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(depth, key, site):
  if depth > 0:
    if key in site:
      return site[key]

    for value in site.values():
      if isinstance(value, dict):
        res = find_key(depth - 1, key, value)
        if res:
          return res
    else:
      return None

key = input("Введите ключ: ")
depth = int(input("Введите грлубину: "))
value = find_key(depth, key, site)
if value:
  print(value)
else:
  print("На такой глубине сайта, ключа нет!")

