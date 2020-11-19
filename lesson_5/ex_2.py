def strange_counter(inc_file):
    count = 0

    try:
        with open(inc_file, 'r', encoding='utf-8') as my_file:
            for i in my_file:
                count += 1
                print(f'{len(i.split())} слов в строке')
            else:
                print(f'всего {count} строк')

    except FileNotFoundError as err:
        print(err)


strange_counter('file_2.txt')
