def sum_from_string():
    cancel_symbol = '-'
    cancel = False
    result = 0
    while not cancel:
        incoming_string = input(f'введите числа через пробел, для окончания ввода введите "{cancel_symbol}": ')
        for i in incoming_string.split():
            if i == cancel_symbol:
                cancel = True
                break
            result = result + float(i)

        print(f'сумма введенных чисел: {result}')


sum_from_string()
