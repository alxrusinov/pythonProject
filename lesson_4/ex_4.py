initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def unique_list(income_list):
    return [item for item in income_list if income_list.count(item) == 1]


print(unique_list(initial_list))
