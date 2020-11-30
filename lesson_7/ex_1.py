def validate_matrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in matrix:
        if len(i) == col:
            continue
        else:
            raise ValueError(f'Матрица {matrix} задана неверно')
    else:
        return row, col


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        shape_self = validate_matrix(self.matrix)
        shape_other = validate_matrix(other.matrix)

        if shape_self[0] == shape_other[0] and shape_self[1] == shape_other[1]:
            result = []
            for rowIndex, row in enumerate(self.matrix):
                result.append([])
                for colIndex, value in enumerate(row):
                    result[rowIndex].append(other.matrix[rowIndex][colIndex] + value)

            return Matrix(result)

        else:
            raise ValueError('Размерность матриц не совпадает')

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += f'{" ".join(map(str, row))}\n'

        return result


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[11, 12], [13, 14], [15, 16]])
matrix_3 = Matrix([[100, 200], [300, 400]])
matrix_4 = Matrix([[111, 222], [333, 444, 555]])

print(matrix_1, end='\n')
print(matrix_2, end='\n')
print(matrix_3, end='\n')
print(matrix_4, end='\n')

print(matrix_1 + matrix_2, end='\n')
print(matrix_1 + matrix_3, end='\n')
