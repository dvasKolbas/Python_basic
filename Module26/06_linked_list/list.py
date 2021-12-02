class LinkedList:
    def __init__(self, name= None, lastValue= None):
        self.name = name
        self.lastValue = lastValue

    def append(self, value):
        if self.lastValue != None:
            self.lastValue.append(value)
        else:
            self.lastValue = LinkedList(value)

    def __str__(self):
        if self.name == None:
            return "[" + str(self.lastValue)
        elif self.lastValue == None:
            return str(self.name) + "]"
        else:
            return str(self.name) + " " + str(self.lastValue)

    def get(self, num, count= -1):
        try:
            if count == num:
                return self.name
            elif self.lastValue == None and num > count:
                raise StopIteration
            else:
                return self.lastValue.get(num, count + 1)
        except StopIteration:
            print("Значение выходит за пределы списка!")

    def remove(self, num, count= -1):
        try:
            if count == num:
                 return self.lastValue
            elif self.lastValue == None and num > count:
                raise StopIteration
            else:
                new_lastValue = self.lastValue.remove(num, count + 1)
                if new_lastValue != None:
                    self.lastValue = new_lastValue
                else:
                    return  None
        except StopIteration:
            print("Значение выходит за пределы списка!")






