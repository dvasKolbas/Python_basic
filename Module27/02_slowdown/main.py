import time
from typing import Callable, Any

def freeze(func: Callable) -> Any:
    """
    Декоратор, замедляющий работу функции на 5 сек.
    """

    def wrapped_func():
        time.sleep(5)
        # start_time = time.time()
        # while True:
        #     if time.time() - start_time >=5:
        #         break
        func()

    return wrapped_func

@freeze
def test():
    print('<Тут что-то происходит...>')


test()
