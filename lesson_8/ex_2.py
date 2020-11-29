class CustomZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


def divide(one, two):
    try:
        if two == 0:
            raise CustomZeroDivisionError('на ноль делить нельзя')
    except CustomZeroDivisionError as error:
        print(error)
    else:
        return one / two


print(divide(3, 4))
print(divide(3, 0))
