from itertools import count, cycle


# Итератор с count
def iterator(start):
    for i in count(start):
        if i > 10:
            break
        print(i)


iterator(3)


# Итератор с cycle
def cycle_iterator(income_list):
    my_iter = cycle(income_list)
    max_iteration = len(income_list) * 4
    iteration = 0
    while iteration < max_iteration:
        print(next(my_iter))
        iteration += 1


cycle_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
cycle_iterator(cycle_list)
