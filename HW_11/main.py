# Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц


class Matrix:

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            return f'Ошибка: матрицы разных размеров'
        else:
            return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])

    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            return f'Ошибка: невозможно перемножить матрицы'
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            return f'Ошибка: матрицы разных размеров'
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            return True

    def __str__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i]) + '\n'
        return s


mx_1 = [[1, 2, 3],
        [4, 5, 6],
        [-1, 4, 0],
        [7, -5, 11]]

mx_2 = [[3, 2, 1],
        [6, 5, 4],
        [-5, 9, 0],
        [9, -3, 10]]

mx_3 = [[1, 2, 3, 4],
        [0, 9, -8, 7],
        [-4, 10, 1, 5]]

mx_4 = [[1, 2, 3, 4, 5],
        [5, 6, 7, 8, 9],
        [-5, -4, -3, -2, -1]]

matr_1 = Matrix(mx_1)
matr_2 = Matrix(mx_2)
matr_3 = Matrix(mx_3)
matr_4 = Matrix(mx_4)

print ("Cложение матриц:")
matr_sum = matr_1 + matr_2
print(matr_sum)

print ("Умножение матриц:")
matr_multiply = matr_1 * matr_3
print(matr_multiply)
print(matr_1 * matr_4)

print ("Cравнение матриц:")
print(matr_1 == matr_1)
print(matr_1 == matr_2)
