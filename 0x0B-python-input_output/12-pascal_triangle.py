#!/usr/bin/python3
"""returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n

    Args:
        n (int): size of Pascal's triangle
    """
    if n < 1:
        return []

    new_list = [[1]]

    for row in range(2, n + 1):
        temp = [1]
        for col in range(1, row - 1):
            temp.append(new_list[-1][col] + new_list[-1][col - 1])
        temp.append(1)
        new_list.append(temp)
    return new_list

