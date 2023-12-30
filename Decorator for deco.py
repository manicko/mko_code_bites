from functools import wraps


def decorator(f):
    def inner(func):
        @wraps(func)
        def inner2(*args, **kwargs):
            return f(func,*args, **kwargs)
        return inner2
    return inner


@decorator
def introduce(f, *args, **kwargs):
    print(f.__name__)
    return f(*args, **kwargs)


@introduce
def identity(x):
    return x


print(identity(31415))


