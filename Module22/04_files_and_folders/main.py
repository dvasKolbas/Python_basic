import os

def count_dir(dir):
    subdirectory = 0
    files = 0
    size = 0
    for elem in os.listdir(dir):
        path = os.path.join(dir, elem)
        if os.path.isdir(path):
            subdirectory += 1
            attachments = count_dir(path)
            subdirectory += attachments[0]
            files += attachments[1]
            size += attachments[2]
        else:
            files += 1
            size += os.path.getsize(path)
    return subdirectory, files, size

dir = os.path.abspath(os.path.join("..", "..","Module14"))
subdirectory, files, size = count_dir(dir)
print("Размер каталога (в Кб):", size/1024)
print("Количество подкаталогов:", subdirectory)
print("Количество файлов:", files)