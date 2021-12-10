from typing import Callable

def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """Декоратор для декораторов, с возможностью передавать любые переменные"""
    def wrapper_decor(*args, **kwargs):
        def func_decor(func: Callable) -> Callable:
            print("Переданные арги и кварги в декоратор:", *args, **kwargs)
            res = decorator(func)
            return res
        return func_decor
    return wrapper_decor



@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def function(text: str, num: int) -> None:
    print("Привет", text, num)


function("Юзер", 101)