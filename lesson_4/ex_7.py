def fact(n):
    accumulator = 1
    for i in range(1, n + 1):
        accumulator = accumulator * i
        yield accumulator


for el in fact(12):
    print(el)