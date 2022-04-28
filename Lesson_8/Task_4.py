from functools import wraps

def val_checker(func_cond):

        def checker(func):
            @wraps(func)
            def wrapper(*args):
                if func_cond(*args):
                    result = func(*args)
                    msg = print(f'{func.__name__}: {result}')
                    return msg
                raise ValueError from ValueError

            return wrapper

        return checker






@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


d = calc_cube(44)
