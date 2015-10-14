#!/usr/bin/env python3
# tetris.py version 0.1


class Cell(object):

    def __init__(self, row, col):
        self.cell = '.'
        self.row = row
        self.col = col

    def get_cell_char(self):
        return self.cell

    def set_cell(self, char):
        self.cell = char


class Matrix(object):
    def __init__(self):
        self.matrix = [[Cell(row, col) for col in range(10)] for row in range(22)]

    def set_matrix_cell(self, row, col, char):
        self.matrix[row][col].set_cell(char)

    def get_string_matrix(self):
        return ''.join([' '.join([elem.get_cell_char() for elem in item]) + '\n' for item in self.matrix])

    def set_matrix(self, file_name):
        try:
            with open(file_name) as fh:
                for row_nr, row in enumerate(fh):
                    for col_nr in range(0, len(row) - 1, 2):
                        if row[col_nr] != ' ':
                            self.matrix[row_nr][col_nr // 2].set_cell(row[col_nr])
        except EnvironmentError as err:
            print(err)


if __name__ == "__main__":
    answer = input()

    # test 2
    if answer == 'p':
        m2 = Matrix()
        print(m2.get_string_matrix())

    # test 3
    if answer == 'g':
        m3 = Matrix()
        m3.set_matrix('input_test3.txt')
        print(m3.get_string_matrix())
