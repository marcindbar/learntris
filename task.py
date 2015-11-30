# test 1
def quit_game(geme):
    exit()

# test 2
def print_game_grid(game):
    print(game.get_grid().get_str_matrix())

# test 3
def set_game_grid(game):
    game.get_grid().set_matrix()

# test 4
def clean_game_grid(game):
    game.get_grid().clear_matrix()

# test 5
def print_game_score(game):
    print(game.get_score())

# test 6
def print_game_cleand_lines(game):
    print(game.get_cleared_lines())

# test 7
def update_score_table(game):
    for row in game.get_grid().matrix:
        if game.get_grid().is_row_full(row):
            game.get_grid().clear_row(row)
            game.update_cleared_lines()
            game.update_score()

# test 8-14 part1
def activate_tetramino(game):
    try:
        game.grid.set_active_tetramino(game.next_command)
    except KeyError as err:
        print(err)

# test 8-14 part2
def print_active_tetramino(game):
    try:
        print(game.grid.available_tetraminos[game.grid.active_tetramino].get_str_grid())
    except:
        print("No tetramino is available")

# test 15-17
def rotate_tetramino_clockwise(game):
    game.grid.available_tetraminos[game.grid.active_tetramino].clockwise()

# test 18-21
def print_newline(game):
    print()

# test 22-23
def print_game_status(game):
    game.set_grid_status()
    print(game.get_grid().get_str_matrix())

# test 24-29
def move_left(game):
    if game.grid.coor['x_axis'] > 0:
        game.grid.coor['x_axis'] -= 1

# test 30
def move_right(game):
    if game.grid.coor['x_axis'] < game.grid.cols:
        game.grid.coor['_axis'] += 1
