


def type_logger(func):

    def wrapper(*args):
        result = func(*args)
        msg = print(f'{func.__name__}: {result}, {type(result)}')
        return msg
    return wrapper




@type_logger
def calc_cube(x):
    return [x ** 3, x, x + 100]


a = calc_cube(3)