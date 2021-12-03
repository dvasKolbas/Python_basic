from typing import Callable, Any

def how_are_you(func: Callable) -> Any:
    """
    Декоратор, сообщающий состояние искусственного интеллекта,
    при запуске функции.
    """

    def wrapped_func():
        answer = input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        func()

    return wrapped_func

@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()