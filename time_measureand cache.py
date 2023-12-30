from time import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = time()
        res = func(*args, **kwargs)
        e = time()
        print(f'{func.__name__} execution time: {s - e}')
        return res

    return wrapper


def cache_it(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper



@cache_it
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)



@cache_it
def double_fact(n: int) -> int:
    if n < 3:
        return n
    return n * double_fact(n - 2)



@measure_time
def colatz(n):
    while n != 1:
        n = (3*n+1) if n%2 else (n//2)
    return n


@measure_time
def get_combin(n: int, k:int) -> int:
    if k == 0 or k == n:
        return 1
    return get_combin(n - 1, k) + get_combin(n - 1, k - 1)

print(double_fact(10))
# double_fact(7) => 105
# double_fact(4) => 8
# double_fact(1) => 1
# double_fact(10) => 3840
print(colatz(9213123123873474987913891749871948719749174917))

print(get_combin(200, 2))

# get_combin(5, 5) => 1
# get_combin(5, 2) => 10
# get_combin(3, 1) => 3
# get_combin(7, 0) => 1