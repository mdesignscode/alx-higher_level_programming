"""Divide all elements of a matrix
matrix must be a list of lists of integers or floats
Each row of the matrix must be of the same size
div must be a number (integer or float)
div can’t be equal to 0
division will be rounded to 0
"""


from lib2to3.pytree import type_repr


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        matrix (list[list[int/float]]): a list of lists of integers or floats.
        div (int/float): number to divide all elements by
    """
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_list = []
    for row in range(len(matrix)):
        if not isinstance(matrix[row], list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        first_row = len(matrix[0])
        if len(matrix[row]) != first_row:
            raise TypeError('Each row of the matrix must have the same size')
        new_list.append([])
        for col in range(len(matrix[row])):
            if type(matrix[row][col]) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            new_list[row].append(round((matrix[row][col] / div), 2))
    return new_list
