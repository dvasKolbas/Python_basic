import functools
from time import time
from typing import Callable
from datetime import datetime

def func_name(func: Callable) -> str:
    """
    Функция для нахождения имени функции с именем класса.
    :param func: Функция
    :return: Имя функции с именем класса
    """
    for i in str(func).split():
        if func.__name__ in i:
            return i

def log_methods(date_format: str) -> Callable:
    def log_decorator(func: Callable) -> Callable:
        """
        Декоратор логирования методов класса
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            start = time()
            time_f = datetime.now().strftime(date_format)
            print(args[0].__class__.__name__)
            print("- Запускается {name}. Дата и время запуска: {time}".format(name= func_name(func), time=time_f))
            res = func(*args, **kwargs)
            print("- Завершение {name}. Время работы: {time}".format(name= func_name(func), time=time() - start))
            return res
        return wrapper
    return log_decorator

def for_all_methods(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и применяет его ко всем методам класса
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for method_name in dir(cls):
            if not method_name.startswith("__"):
                cur_method = getattr(cls, method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, method_name, decorated_method)
        return cls
    return decorate



@for_all_methods(log_methods("%b %d %Y - %H:%M:%S"))
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@for_all_methods(log_methods("%b %d %Y - %H:%M:%S"))
class B(A):
    pass
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
