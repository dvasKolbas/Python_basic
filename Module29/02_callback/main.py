from typing import Callable

app = dict()


def callback(key: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        app[key] = func
        return func

    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
