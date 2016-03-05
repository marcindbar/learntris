from commands import execute


class Cell(object):

    def __init__(self, char='.'):
        self.cell = char

    def get_cell_char(self):
        return self.cell

    def set_cell(self, char):
        self.cell = char


class Matrix(object):

    def __init__(self, body=None, cols=10, rows=22):
        self.cols = cols
        self.rows = rows
        if body is None:
            self.matrix = [[Cell() for col in range(cols)] for row in range(rows)]
        else:
            self.matrix = [[Cell(col.get_cell_char()) for col in row] for row in body]
        self.active_tetramino = ''
        self.active = None
        self.available_tetraminos = {}
        self.load_tetraminos('tetraminos.txt')
        self.coor = {'x_axis':0, 'y_axis':0}

    def get_str_matrix(self):
        return '\n'.join([' '.join([col.get_cell_char() for col in row]) for row in self.matrix])

    def set_matrix(self, rows=22):
        new_body = [item.split(' ') for item in [input() for dummy in range(rows)]]
        for row_nr, row in enumerate(self.matrix):
            for cell_nr, cell in enumerate(row):
                cell.set_cell(new_body[row_nr][cell_nr])

    def clear_matrix(self):
        for row in self.matrix:
            for col in row:
                col.set_cell('.')

    def is_row_full(self, row):
        for cell in row:
            if cell.get_cell_char() == '.':
                return False
        return True

    def clear_row(self, row):
        for cell in row:
            cell.set_cell('.')

    def copy_tetramino(self, name):
        old = self.available_tetraminos[name]
        tet = Tetramino(name, old.get_body())
        self.active = tet
        return self.active

    def set_active_tetramino(self, active_item):
        self.active_tetramino = active_item
        x = (self.cols-self.available_tetraminos[self.active_tetramino].get_width())//2
        self.coor = {'x_axis':x, 'y_axis':0}
        self.copy_tetramino(active_item)

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

    def settle_tetramino(self):
        if self.active_tetramino != '':
            tetra = self.active
            x, y = self.coor['x_axis'], self.coor['y_axis']
            dx, dy = tetra.get_hight(), tetra.get_width()
            for y_dy in range(y,y+dy):
                for x_dx in range(x,x+dx):
                    if self.matrix[y_dy][x_dx].get_cell_char() == '.':
                        self.matrix[y_dy][x_dx].set_cell(tetra.grid[y_dy-y][x_dx-x].get_cell_char())
            self.active_tetramino = ''

    def clear_tetramino(self):
        tetra = self.active
        x, y = self.coor['x_axis'], self.coor['y_axis']
        dx, dy = tetra.get_hight(), tetra.get_width()

        for y_dy in range(y,y+dy):
            for x_dx in range(x,x+dx):
                if tetra.grid[y_dy-y][x_dx-x].get_cell_char() != '.':
                    self.matrix[y_dy][x_dx].set_cell('.')

    def check_collisions(self, x, y):
        tetra = self.active
        for y_pos in range(tetra.get_hight()):
            for x_pos in range(tetra.get_width()):
                if tetra.grid[y_pos][x_pos].get_cell_char() != '.' and self.matrix[y+y_pos][x+x_pos].get_cell_char() != '.':
                    return True
        return False


class Tetramino(object):

    def __init__(self, name, body):
        self.name = name
        self.grid = [[Cell(char) for char in row] for row in body]
        self.body = body

    def get_body(self):
        return self.body

    def get_str_grid(self):
        return '\n'.join([' '.join([col.get_cell_char() for col in row]) for row in self.grid])

    def clockwise(self):
        self.grid = [item for item in zip(*self.grid[::-1])]

    def anticlockwise(self):
        self.grid = [item for item in list(zip(*self.grid))[::-1]]

    def is_right_free(self):
        for row in self.grid:
            if row[-1].get_cell_char() != '.':
                return False
        return True

    def shift_right(self):
        if self.is_right_free():
            for col in range(self.get_width() - 2, -1, -1):
                for row in range(self.get_hight()):
                    self.grid[row][col+1].set_cell(self.grid[row][col].get_cell_char())
            for row in range(self.get_hight()):
                self.grid[row][0].set_cell('.')

    def is_left_free(self):
        for row in self.grid:
            if row[0].get_cell_char() != '.':
                return False
        return True

    def shift_left(self):
        if self.is_right_free():
            for col in range(1, self.get_width() - 1):
                for row in range(self.get_hight()):
                    self.grid[row][col-1].set_cell(self.grid[row][col].get_cell_char())
            for row in range(self.get_hight()):
                self.grid[row][-1].set_cell('.')

    def is_down_free(self):
        for col in self.grid[-1]:
            if col.get_cell_char() != '.':
                return False
        return True

    def shift_down(self):
        if self.is_down_free():
            for row in range(self.get_hight() - 2, -1, -1):
                for col in range(self.get_width()):
                    self.grid[row+1][col].set_cell(self.grid[row][col].get_cell_char())

            for col in range(self.get_width()):
                self.grid[0][col].set_cell('.')

    def is_up_free(self):
        for col in self.grid[0]:
            if col.get_cell_char() != '.':
                return False
        return True

    def shift_up(self):
        if self.is_up_free():
            for row in range(self.get_hight() - 1):
                for col in range(self.get_width()):
                    self.grid[row][col].set_cell(self.grid[row+1][col].get_cell_char())

            for col in range(self.get_width()):
                self.grid[-1][col].set_cell('.')

    def get_hight(self):
        return len(self.grid)

    def get_width(self):
        return len(self.grid[0])


class Game(object):
    messages = {
        'title': 'Learntris (c) 1992 Tetraminex, Inc.\nPress start button to begin.',
        'pause': 'Paused\nPress start button to continue.',
    }

    def __init__(self):
        self.score = 0
        self.cleared_lines = 0
        self.grid = Matrix()
        self.queued_answers = ''
        self.counter_queue = 0
        self.next_command = ''
        self.all_commands = execute.keys()
        self.app_state = None

    def get_grid(self):
        return self.grid

    def get_grid_with_tetramino(self):
        if self.grid.active_tetramino != '':
            new_matrix = Matrix(self.grid.matrix)
            tetra = self.grid.active
            x, y = self.grid.coor['x_axis'], self.grid.coor['y_axis']
            dx, dy = tetra.get_hight(), tetra.get_width()
            for y_dy in range(y,y+dy):
                for x_dx in range(x,x+dx):
                    if tetra.grid[y_dy-y][x_dx-x].get_cell_char() != '.':
                        new_matrix.matrix[y_dy][x_dx].set_cell(tetra.grid[y_dy-y][x_dx-x].get_cell_char().upper())
            return new_matrix
        return self.get_grid()

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

    def get_grid_status(self):
        return self.get_grid_with_tetramino()
