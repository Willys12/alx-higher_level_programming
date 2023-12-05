#!/usr/bin/pythn3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        f_row = " ".join("{:<2}".format(element) for element in row)
        print(f_row)
