#!/usr/bin/python3
"""
that returns a list of lists of integers representing the Pascal’s triangle of n 
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    final_list = []
    if n <= 0:
        return final_list
    # add first 1
    if n > 0:
        final_list.append([1])

    # add second level
    if n > 1:
        final_list.append([1, 1])

    for i in range(3, n + 1):
        final_list.append([0] * i)

        # set 1st and last 1
        final_list[i-1][0] = 1
        final_list[i-1][i-1] = 1

        #calculate middle numbers
        for j in range(1, i - 1):
            final_list[i-1][j] = \
                    final_list[i-2][j-1] + final_list[i-2][j]

    return final_list
