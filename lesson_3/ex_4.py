def my_func(base, degree):
    return (1 / base) ** abs(degree)


def my_func2(base, degree):
    transformed_base = 1 / base
    result = 1

    for i in range(abs(degree)):
        result = result * transformed_base

    return result


print(my_func(2, -14))
print(my_func2(2, -14))
