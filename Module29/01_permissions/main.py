from typing import Callable, List

def check_permission(required_permission: str, user_permissions: List[str]) -> Callable:
    def permossion_decorator(func: Callable) -> Callable:
        def wrapped(*args, **kwargs):
            try:
                if not required_permission in user_permissions:
                    raise PermissionError
                else:
                    func(*args, **kwargs)
            except PermissionError as error:
                print("PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {name}".format(name=func.__name__))
            return func
        return wrapped
    return permossion_decorator

user_permissions = ['admin']

@check_permission('admin', user_permissions)
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1', user_permissions)
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()