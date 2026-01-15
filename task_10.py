import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.name} took {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def heavy_computation(n):
    return sum(i * i for i in range(n))


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
filtered = list(filter(lambda x: x > 10, squared))
