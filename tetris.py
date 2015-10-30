#!/usr/bin/env python3
# tetris.py version 0.1


class Cell(object):
    def __init__(self, char='.'):
        self.cell = char

    def get_cell_char(self):
        return self.cell

    def set_cell(self, char):
        self.cell = char


class Matrix(object):
    def __init__(self, cols=10, rows=22):
        self.cols = cols
        self.rows = rows
        self.matrix = [[Cell() for col in range(cols)] for row in range(rows)]

    def get_string_matrix(self):
        return '\n'.join([' '.join([elem.get_cell_char() for elem in item]) for item in self.matrix])

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


class Game(object):
    def __init__(self):
        self.score = 0
        self.matrix = Matrix()

    def get_score(self):
        return self.score

    def get_matrix(self):
        return self.matrix

if __name__ == "__main__":
    g = Game()
    m = g.get_matrix()

    answer = input()
    while answer != 'q':
        # test 2
        if answer == 'p':
            print(m.get_string_matrix())

        # test 3
        if answer == 'g':
            m.set_matrix('input_test3.txt')
            m.get_string_matrix()

        # test 4
        if answer == 'c':
            m.clear_matrix()
            m.get_string_matrix()

        # test 5
        if answer == '?s':
            print(g.get_score())


        answer = input()
