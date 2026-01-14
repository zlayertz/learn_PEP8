x_value = 1 + 2 * 3 - 4 / 5
list1 = [1, 2, 3, 4, 5]
dict1 = {'a': 1, 'b': 2, 'c': 3}


def func(a=0, b=0):
    return a ** 2 + b ** 2


result = func(a=2, b=3)
if 10 < result < 20:
    print("Result in range")