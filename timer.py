from time import time


class timer():
    '''Measures function execution time in milliseconds'''

    def __init__(self, num_runs):
        self.num_runs = num_runs

    def __call__(self, func, *args, **kwargs):
        def timer(*args, **kwarg):
            start = time()
            for _ in range(self.num_runs):
                res = func(*args, **kwargs)
            end = time()
            elapsed = (end - start) / self.num_runs * 1000
            print(f'[runs: {self.num_runs} | average time: {elapsed:.6f} ms]')
            return res
        return timer

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        pass


def fibonacci(n):
    a, b = 0, 1
    if n < 0:
        return
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a, b = b, c
        return b

 # ______________ context __________________


with timer(num_runs=10) as t:
    t(fibonacci)(10000)

 # ______________ decorator _________________


@timer(num_runs=10)
def fibonacci(n):
    a, b = 0, 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a, b = b, c
        return b


res = fibonacci(10000)
