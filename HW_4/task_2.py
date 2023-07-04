# Напишите функцию для транспонирования матрицы'''


def transpon_matrix(matrix_1):
    '''Сначала, создаем целевую матрицу с размерностью повёрнутой исходной.
    Затем, заполняем целевую матрицу элементами исходной, во вложенных циклах'''
    matrix_2 = [0] * len(matrix_1[0])
    for i in range(len(matrix_1[0])):
        matrix_2[i] = [0] * len(matrix_1)
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            matrix_2[j][i] = matrix_1[i][j]
    return matrix_2


def print_matrix(matrix):
    '''Функция печати матрицы в терминал'''
    for i in range(len(matrix)):
        print(matrix[i])


# Создаём исходную матрицу
original_matrix = [[11,12,13,14], [21,22,23,24], [31,32,33,34]]

print('Исходная матрица:')
print_matrix(original_matrix)
print('\n'+'Транспонированная матрица:')
print_matrix(transpon_matrix(original_matrix))