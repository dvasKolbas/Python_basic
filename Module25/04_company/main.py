import random

import person

peoples = [person.Manager("Вадим", "Иванов", random.randint(20, 50), 13000),
           person.Manager("Максим", "Петров", random.randint(20, 50), 13000),
           person.Manager("Василий", "Сидоров", random.randint(20, 50), 13000),
           person.Agent("Иван", "Кузнецов", random.randint(20, 50), 130000),
           person.Agent("Мария", "Иванова", random.randint(20, 50), 150000),
           person.Agent("Руслан", "Зайцев", random.randint(20, 50), 230000),
           person.Worker("Анна", "Васильева", random.randint(20, 50), 50),
           person.Worker("Михаил", "Сергеев", random.randint(20, 50), 100),
           person.Worker("Алексей", "Соболев", random.randint(20, 50), 150)]

for people in peoples:
     people.print_salary()