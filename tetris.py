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
        return '\n'.join([' '.join([col.get_cell_char() for col in row]) for row in self.matrix])

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

    def is_row_full(self, row):
        for cell in row:
            if cell.get_cell_char() == '.':
                return False
        return True

    def clear_row(self, row):
        for cell in row:
            cell.set_cell('.')


class Tetramino(object):
    def __init__(self, name, body):
        self.name = name
        self.grid = [[Cell(char) for char in row] for row in body]

    def get_string_grid(self):
        return '\n'.join([' '.join([col.get_cell_char() for col in row]) for row in self.grid])


class Game(object):
    def __init__(self):
        self.score = 0
        self.cleared_lines = 0
        self.grid = Matrix()
        self.active_tetramino = ''
        self.available_tetraminos = {}

    def get_grid(self):
        return self.grid

    def get_score(self):
        return self.score

    def update_score(self):
        self.score += 100

    def get_cleared_lines(self):
        return self.cleared_lines

    def update_cleared_lines(self):
        self.cleared_lines += 1

    def load_tetraminos(self, input_file_name):
        try:
            with open(input_file_name) as fh:
                for item in fh.read().split('#\n'):
                    (grid, name) = item.split('\n@')
                    body = [row.split(' ') for row in grid.split('\n')]
                    tetramino = Tetramino(name, body)
                    self.available_tetraminos.update({name.rstrip(): tetramino})
        except:
            print("Unexpected error.")

    def set_active_tetramino(self, active_item):
        self.active_tetramino = active_item

if __name__ == "__main__":
    game = Game()
    grid = game.get_grid()

    answer = input()
    while answer != 'q':
        # test 2
        if answer == 'p':
            print(grid.get_string_matrix())

        # test 3
        if answer == 'g':
            grid.set_matrix('input_test3.txt')

        # test 4
        if answer == 'c':
            grid.clear_matrix()

        # test 5
        if answer == '?s':
            print(game.get_score())

        # test 6
        if answer == '?n':
            print(game.get_cleared_lines())

        # test 7
        if answer == 's':
            grid.set_matrix('input_test7.txt')
            for row in grid.matrix:
                if grid.is_row_full(row):
                    grid.clear_row(row)
                    game.update_cleared_lines()
                    game.update_score()

        # test 8
        if answer == 't':
            game.load_tetraminos('tetraminos.txt')
            game.set_active_tetramino('I')
            print(game.available_tetraminos['I'].get_string_grid())

        answer = input()
