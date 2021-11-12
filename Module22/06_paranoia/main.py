def cipher_text(file, a = "abcdefghijklmnopqrstuvwxyz"):
    new_text = ""
    for line_id, line in enumerate(file):
        new_text += "".join([a[a.index(i.lower()) + (line_id + 1)]
                             for i in line if i.lower() in a]).title() \
                    + "\n"
    return new_text

file = open("text.txt", "r")
cipher_file = open("cipher_file.txt", "w")
cipher_file.write(cipher_text(file))
file.close()
cipher_file.close()