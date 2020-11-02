number = int(input('введите положительное число '))

if number <= 0:
    number = int(input('введите положительное число '))
else:
    max_number = 0
    for i in str(number):
        if int(i) == 9:
            max_number = int(i)
            break
        if int(i) > max_number:
            max_number = int(i)

    print(f'самая большая цифра в числе {number} - {max_number}')
