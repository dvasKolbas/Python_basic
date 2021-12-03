from typing import Callable, Any

def debug(func: Callable) -> Any:
    """
    Декоратор вывода наименования, аргументов и результата функции
    """
    def wrapped_func(*args, **kwargs):
        param = ""
        if len(args) > 0:
            param += '"' + '", "'.join(args) + '"'
        if len(args) > 0 and len(kwargs) > 0:
            param += ', '
        if len(kwargs) > 0:
            param += ", ".join(list((key +"="+ str(value)) if isinstance(value, int) else (key +'="'+ value +'"') for key, value in kwargs.items()))
        print('Вызывается {name}({param})'.format(name=func.__name__, param=param))
        res = func(*args, **kwargs)
        print("'{name}' вернула значение '{res}'".format(name=func.__name__, res=res))
        print(res +"\n")

    return wrapped_func



@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)