# Exercise 7.10

from time import time

def timethis(func):
    def timed_func(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"{func.__module__}.{func.__name__}: {end - start:.2f} s")
    return timed_func
