class Node:
    def __init__(self, name= None, next= None):
        self.name = name
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            next = self.head
            while next.next:
                next = next.next
            next.next = Node(value)

    def __str__(self):
        if self.head == None:
             return "нет значений"
        else:
            next = self.head
            string = "[" + str(next.name)
            while next.next:
                next = next.next
                string +=" " + str(next.name)
            return string + "]"



    def get(self, num):
        if self.head == None:
             return "нет значений"
        else:
            count = 0
            next = self.head
            while next:
                if num == count:
                    return next.name
                next = next.next
                count += 1
            else:
                return "индекс за пределами списка"

    def remove(self, num):
        if self.head != None:
            if num == 0:
                self.head = self.head.next
                return
            count = 1
            next = self.head
            while next:
                if num == count:
                    if next.next.next == None:
                        next.next = None
                    else:
                        next.next = next.next.next
                    return
                next = next.next
                count += 1
            else:
                return "индекс за пределами списка"






