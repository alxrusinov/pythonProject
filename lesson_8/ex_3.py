def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


class OnlyNumberError(Exception):
    def __init__(self, value, msg='must be a number'):
        self.value = value
        self.msg = msg

    def __str__(self):
        return f'{self.value} {self.msg}'


def get_number_list():
    my_list = []
    while True:
        new_item = input('Введите очередное число для списка, для окончания ввода введите "stop":\n')
        if new_item == 'stop':
            break
        try:
            if is_number(new_item):
                transformed_item = float(new_item) if '.' in new_item else int(new_item)
                my_list.append(transformed_item)
            else:
                raise OnlyNumberError(new_item)
        except OnlyNumberError as error:
            print(error)
            continue

    return my_list


print(get_number_list())
