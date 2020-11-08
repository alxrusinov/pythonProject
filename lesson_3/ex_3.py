def my_func(first, second, third):
    return sum(sorted((first, second, third), reverse=True)[:2])


print(my_func(100, 56, 10))
