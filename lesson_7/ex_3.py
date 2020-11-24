class Cell:
    _cell_symbol = '*'

    def __init__(self, cells):
        self._cells = cells

    @property
    def cells(self):
        return self._cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            raise ValueError('Итоговое количество клеток быть больше нуля')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        div = round(self.cells / other.cells)
        if div > 0:
            return Cell(div)
        else:
            raise ValueError('Итоговое количество клеток быть больше нуля')

    def __str__(self):
        return f'{self.cells} cells'

    def make_order(self, cell_in_row):
        result = []
        rest = self.cells
        while rest > 0:
            item = str(self._cell_symbol * cell_in_row) if rest > cell_in_row else str(self._cell_symbol * rest)
            result.append(item)
            rest -= cell_in_row

        return '\n'.join(result)


cell_1 = Cell(15)
cell_2 = Cell(38)

print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_2 * cell_1)
print(cell_2 / cell_1)
print('=' * 124)
print(cell_1.make_order(4))
print('=' * 124)
print(cell_2.make_order(7))
print('=' * 124)
try:
    cell_1 - cell_2
except ValueError as error:
    print(error)
print('=' * 124)
try:
    cell_1 / cell_2
except ValueError as error:
    print(error)
