def divide(first_number=input('введите делимое: '), second_number=input('введите делитель: ')):
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        return first_number / second_number
    except ValueError:
        print('ведите корректные числа')
    except ZeroDivisionError:
        print('на ноль делить нельзя!')


print(divide())
