initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def strange_filter(income_list):
    return [item for index, item in enumerate(income_list) if index != 0 and item > income_list[index - 1]]


print(strange_filter(initial_list))
