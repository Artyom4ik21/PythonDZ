from functools import wraps
def type_logger(func):

    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        types = [f'{i}: {type(i)}' for i in args]
        print(f'{func.__name__}({", ".join(types)})')
        return result
    return wrapper

@type_logger
def calc_cube(x):
    return x**3

@type_logger
def calc_func(x, y):
    return x**3 + y

print(calc_cube(3))
print(calc_func(3,1)) 