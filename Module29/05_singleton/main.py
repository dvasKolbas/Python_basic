from typing import Callable

def singleton(cls: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        if wrapper.instance is None:
            wrapper.instance = instance
        return wrapper.instance
    wrapper.instance = None
    return wrapper


@singleton
class Example:
    pass




my_obj = Example()
my_another_obj = Example()


print(id(my_obj))
print(id(my_another_obj))


print(my_obj is my_another_obj)
