# Замикання
def out_func(x):
    def in_func(y):
        return x + y
    return in_func

clos = out_func(5)
# print(clos(10))



def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

my_c = counter()
# print(my_c())
# print(my_c())
# print(my_c())
# print(my_c())


def mult(x):
    def mult_by(n):
        return x * n
    return mult_by

double = mult(2)
triple = mult(3)

# print(double(5))
# print(triple(5))



# Декоратори

# @decorator_name
# def func_to_decorate():
#     pass


def my_logger(func):
    def wrapper():
        print(f'call function: {func.__name__}')
        return func()
    return wrapper

@my_logger
def say_hi():
    print('Hello, World!')

# say_hi()


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'function was working for: {end_time - start_time} seconds')
        return result
    return wrapper

@timer
def some_func():
    for _ in range(10000000):
        pass

# some_func()



# Анотації

def greet(name: str) -> str:
    return(f'Hello, {name}')

# print(greet('Oleh'))

age: int = 23
# int age = 23.   str name = 'dadasd'

from typing import List, Dict, Set, Tuple, Union, Optional

names: List[str] = ['Alice', 'Boris', 'Cicero']
# print(names)
scores: Dict[str, int] = {'Alice': 27}
uniq: Set[int] = {1,2,3,4}
coords: Tuple[int, int, int] = (10, -2, 8)

def user_inp() -> Union[str, int]:
    pass

def finder(items: list, item_name: str) -> Optional[str]:
    pass

