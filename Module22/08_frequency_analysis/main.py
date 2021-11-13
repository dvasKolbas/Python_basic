def count_letter(text, a = "abcdefghijklmnopqrstuvwxyz"):
    count = {letter:text.count(letter) for letter in a if text.count(letter) > 0}
    summ = sum(count.values())
    count = {i_key:round(i_value/summ, 3) for i_key, i_value in count.items()}
    return count

def sort_letter(count):
    count_sort = sorted(count.items(), key=sort_key, reverse=True)
    string = "\n".join(i[0] + " " + str(i[1]) for i in count_sort)
    return string

def sort_key(k):
    a = "abcdefghijklmnopqrstuvwxyz"
    return k[1] * 10000 - a.index(k[0])

text_file = open("text.txt", "r")
count_dict = count_letter(text_file.read().lower())
text_file.close()

analysis = open("analysis.txt", "w")
analysis.write(sort_letter(count_dict))
analysis.close()