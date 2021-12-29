from functools import wraps


def val_checker(val):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            if val(*args):
                return result
            raise ValueError(f'Wrong val {args}')
        return wrapper
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x**3

@val_checker(lambda x, y: x > 0 and y > 0)
def calc_sum(x, y):
    return x + y

a = calc_cube(5)
print(a)

b = calc_sum(4, 6)
print(b)