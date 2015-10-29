#!/usr/bin/env python3
# tetris.py version 0.1


class Cell(object):
    def __init__(self, row, col, char='.'):
        self.cell = char
        self.row = row
        self.col = col

    def get_cell_char(self):
        return self.cell

    def set_cell(self, char):
        self.cell = char


class Matrix(object):
    def __init__(self, cols=10, rows=22):
        self.cols = cols
        self.rows = rows
        self.matrix = [[Cell(row, col) for col in range(cols)] for row in range(rows)]

    def get_string_matrix(self):
        return ''.join([' '.join([elem.get_cell_char() for elem in item]) + '\n' for item in self.matrix])

    def set_matrix(self, input_file_name):
        try:
            with open(input_file_name) as fh:
                for row_nr, row in enumerate(fh):
                    for col_nr in range(0, len(row) - 1, 2):
                        if row[col_nr] != ' ':
                            self.matrix[row_nr][col_nr//2].set_cell(row[col_nr])
        except EnvironmentError as err:
            print(err)

    def clear_matrix(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.matrix[row][col].set_cell('.')


if __name__ == "__main__":

    m = Matrix()
    answer = input()

    # test 2
    if answer == 'p':
        print(m.get_string_matrix())

    # test 3
    if answer == 'g':
        m.set_matrix('input_test3.txt')
        print(m.get_string_matrix())

    # test 4
    if answer == 'c':
        m.clear_matrix()
        print(m.get_string_matrix())
