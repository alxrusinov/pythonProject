my_list = [7, 5, 3, 3, 2]

new_rating = int(input('введите значение рейтинга '))

if new_rating in my_list:
    index = my_list.index(new_rating)
    count = my_list.count(new_rating)

    my_list.insert(index + count, new_rating)
else:
    if new_rating < min(my_list):
        my_list.append(new_rating)
    elif new_rating > max(my_list):
        my_list.insert(0, new_rating)
    else:
        index = 0
        while my_list[index] > new_rating:
            index += 1

        my_list.insert(index, new_rating)

print(my_list)
