from manager import TaskManager


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.new_task("сделать уборку", 4)

# manager.delete_task(4)
# manager.delete_task(1)
# print()
print(manager)