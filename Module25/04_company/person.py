class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def print_salary(self):
        print(self.__name, self.__surname, "зарабатывает:", end=" ")

class Employee(Person):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.__salary = salary

    def print_salary(self):
        super().print_salary()
        print(self.__salary)

class Manager(Employee):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age, salary)

class Agent(Employee):
    def __init__(self, name, surname, age, sales):
        self.__sales = sales
        super().__init__(name, surname, age, self.calculate_salary())

    def calculate_salary(self):
        salary = round(5000 + (self.__sales * 5 / 100))
        return salary

class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        self.__hours = hours
        super().__init__(name, surname, age, self.calculate_salary())

    def calculate_salary(self):
        salary = 100 * self.__hours
        return (salary)

