from commands import execute

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
        self.active_tetramino = ''
        self.available_tetraminos = {}
        self.load_tetraminos('tetraminos.txt')
        self.coor = {'x_axis':0, 'y_axis':0}

    def get_str_matrix(self):
        return '\n'.join([' '.join([col.get_cell_char() for col in row]) for row in self.matrix])

    def set_matrix(self, rows=22):
        body = [item.split(' ') for item in [input() for dummy in range(rows)]]
        for row_nr, row in enumerate(self.matrix):
            for cell_nr, cell in enumerate(row):
                cell.set_cell(body[row_nr][cell_nr])

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

    def set_active_tetramino(self, active_item):
        self.active_tetramino = active_item
        x = (self.cols-len(self.available_tetraminos[self.active_tetramino]))//2
        self.coor = {'x_axis':x, 'y_axis':0}

    def load_tetraminos(self, input_file_name):
        try:
            with open(input_file_name) as fh:
                for item in fh.read().split('#\n'):
                    (grid, name) = item.split('\n@')
                    body = [row.split(' ') for row in grid.split('\n')]
                    tetramino = Tetramino(name, body)
                    self.available_tetraminos.update({name.rstrip(): tetramino})
        except:
            print("Sorry, tetraminos are not loaded!")

    def set_status(self):
        tetra = self.available_tetraminos[self.active_tetramino]
        for row in tetra.grid:
            for cell in row:
                cell.set_cell(cell.get_cell_char().upper())
        x, y = self.coor['x_axis'], self.coor['y_axis']

        for ind in range(len(tetra)):
            self.matrix[y:y+len(tetra)][ind][x:x+len(tetra)] = tetra.grid[ind]


class Tetramino(object):
    def __init__(self, name, body):
        self.name = name
        self.grid = [[Cell(char) for char in row] for row in body]

    def get_str_grid(self):
        return '\n'.join([' '.join([col.get_cell_char() for col in row]) for row in self.grid])

    def clockwise(self):
        self.grid = [item for item in zip(*self.grid[::-1])]

    def __len__(self):
        return len(self.grid)


class Game(object):

    def __init__(self):
        self.score = 0
        self.cleared_lines = 0
        self.grid = Matrix()
        self.queued_answers = ''
        self.counter_queue = 0
        self.next_command = ''
        self.all_commands = execute.keys()

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

    def set_next_command(self):
        if self.counter_queue < 1:
            answer = input()
            if ' ' in answer:
                new_answer = ''.join([item for item in answer.split(' ')])
                self.counter_queue += len(new_answer)
                self.queued_answers += new_answer
            else:
                self.counter_queue += len(answer)
                self.queued_answers += answer

        if self.queued_answers[0] == '?':
            answer = self.queued_answers[0:2]
            if answer in self.all_commands:
                self.queued_answers = self.queued_answers[2:]
                self.counter_queue -= 2
                self.next_command = answer
        else:
            if self.queued_answers[0] in self.all_commands:
                answer = self.queued_answers[0]
                self.next_command = answer
            self.queued_answers = self.queued_answers[1:]
            self.counter_queue -= 1



    def set_grid_status(self):
        self.grid.set_status()
