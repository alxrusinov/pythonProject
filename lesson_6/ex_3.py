class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position_1 = Position(name='Jhon', surname='Smith', position='developer', income={'wage': 180000, 'bonus': 20000})

print(position_1.name)
print(position_1.surname)
print(position_1.position)
print(position_1._income)
print(position_1.get_full_name())
print(position_1.get_total_income())