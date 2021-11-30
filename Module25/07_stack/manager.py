from stack import Stack
class TaskManager:
    def __init__(self):
        self.task = {}

    def __str__(self):
        string = ""
        for i in sorted(self.task.keys()):
            string += str(i) + " " + str(self.task[i]) + ";\n"
        return string

    def new_task(self, task, priority):
        if not priority in self.task.keys():
            self.task[priority] = Stack()
        self.task[priority].push(task)

    def delete_task(self, priority):
        if not priority in self.task.keys():
            print("Задач с таким приоритетом нет!")
        else:
            print("Удалили задачу:", self.task[priority].pop())
            if len(str(self.task[priority])) == 0:
                self.task.pop(priority)
