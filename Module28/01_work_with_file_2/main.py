import os


class OpenFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        if "file.txt" in os.listdir(os.getcwd()):
            mode = "r"
        else:
            mode = "w"
        self.file = open(self.file_name, mode)
        if mode == "w":
            self.file.write("Test")
            self.file = open(self.file_name, "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True

with OpenFile("file.txt") as file:
    text = file.read()
    print(text)