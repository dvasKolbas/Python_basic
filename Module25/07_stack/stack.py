class Stack:
    def __init__(self):
        self.__list = []

    def __str__(self):
        return str(", ".join(self.__list))

    def push(self, elem):
        self.__list.append(elem)

    def pop(self):
        if len(self.__list) == 0:
            return None
        else:
            return self.__list.pop()
