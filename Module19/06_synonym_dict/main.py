def find_word(synonyms):
    while True:
        word = input("Введите слово: ")
        if synonyms.get(word.title()) != None:
            print(f"Синоним: {synonyms.get(word.title())}")
            break
        else:
            print("Такого слова в словаре нет.")

def create_dict(synonyms, count):
    for i in range(count):
        syn_list = input(f"{i + 1} пара: ").split(" - ")
        synonyms[syn_list[1]] = syn_list[0]
    return synonyms

count = int(input("Dедите количество пар слов: "))
synonyms = create_dict(dict(), count)
print()
find_word(synonyms)
