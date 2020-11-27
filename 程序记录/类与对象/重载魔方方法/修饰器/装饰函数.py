import time

def time_calculate(func):
    def wrapper(a,b):
        start = time.time()
        f = func(a,b)
        exec_time = time.time() - start
        print(exec_time)
        return f
    return wrapper

@time_calculate
def add(a,b):
    return a + b
@time_calculate
def sub(a,b):
    return a - b
add(1,2)