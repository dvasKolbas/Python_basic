alphabet = 'abcdefg'
copy = alphabet

print("Копия:", copy)
print("Элементы строки в обратном порядке:", alphabet[10::-1])
print("Каждый второй элемент строки (включая самый первый):", alphabet[0:10:2])
print("Каждый второй элемент строки после первого:", alphabet[1:10:2])
print("Все элементы до второго:", alphabet[:1])
print("Все элементы, начиная с конца до предпоследнего:", alphabet[6:5:-1])
print("Все элементы в диапазоне индексов от 3 до 4 (не включая 4):", alphabet[3:4])
print("Последние три элемента строки:", alphabet[4:7])
print("Все элементы в диапазоне индексов от 3 до 4 (не включая 5):", alphabet[3:5])
print("То же, что и в предыдущем пункте, но в обратном порядке:", alphabet[4:2:-1])


