def my_func(target_file):
    with open(target_file, 'w+', encoding='utf-8') as my_file:
        input_string = input('введите числа через пробел:\n')
        my_file.write(input_string)
        my_file.seek(0)

        result = 0
        for number in my_file.read().split():
            try:
                result = result + float(number)
            except ValueError as error:
                print(error)

        print(result)


my_func('file_5.txt')
