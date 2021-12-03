from typing import Callable, Any

def counter(func: Callable) -> Any:
    """
    Декоратор подсчета кол-ва вызовов функции
    """
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        func(*args, **kwargs)
        print("Функция {name}, была вызвана: {count}раз".format(name=func.__name__, count=wrapped_func.count))
    wrapped_func.count = 0
    return wrapped_func



@counter
def simple_func(num):
    print(num)

for i in range(5):
    simple_func(i)