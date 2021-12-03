import datetime
import os
from typing import Callable, Any

def logging(func: Callable) -> Any:
    """
    Декоратор логирования ошибок при выполнении функций.
    Ошибки записываются в файл function_errors.log
    """

    def wrapped_func(*args, **kwargs):
        with open("function_errors.log", "a") as log_file:
            try:
                print("Название функции: {name}\n"
                      "Описание функции:"
                      "{description}".format(name=func.__name__, description=func.__doc__))
                return func(*args, **kwargs)
            except Exception as exep:
                string = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") \
                         + " " + func.__name__ + " " + type(exep).__name__ + "\n"
                log_file.write(string)
    return wrapped_func
@logging
def first_func(lst: list) -> None:
    """
    Функция печати списка
    :param lst: Список
    :return: None
    """
    for i in range(5):
        print(lst[i])

@logging
def second_func(fist_num: int, second_num: int) -> float:
    """
    Функция деления одного числа на другое
    :param fist_num: Первое число
    :param second_num: Второе число
    :return: Результат
    """
    return fist_num/second_num

@logging
def third_func(value: Any) -> None:
    """
    Функция преобразования значения в integer
    и вывода на экран
    :param value: Значение
    :return: None
    """
    print(int(value))

def delete_file():
    if "function_errors.log" in os.listdir(os.getcwd()):
        os.remove(os.path.abspath(os.path.join("function_errors.log")))

delete_file()
first_func([i for i in range(4)])
print(second_func(1, 0))
third_func("Не число")
