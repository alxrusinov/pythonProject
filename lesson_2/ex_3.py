season_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень',
               'зима']
season_dict = {(3, 4, 5): 'весна', (6, 7, 8): 'лето', (9, 10, 11): 'осень', (1, 2, 12): 'зима'}

while True:
    month = int(input('введите меся в виде числа от 1 до 12 '))

    if 1 <= month <= 12:
        break

# from list
print(season_list[month - 1])

# from dict
for key in season_dict:
    if month in key:
        print(season_dict[key])
        break
