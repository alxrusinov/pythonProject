from functools import reduce


def my_awesome_function(start, stop):
    return reduce(lambda acc, item: acc * item, [i for i in range(start, stop + 1) if not i % 2])


print(my_awesome_function(100, 1000))
