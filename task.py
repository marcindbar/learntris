# test 1
def quit_game(geme):
    exit()

# test 2
def print_game_grid(game):
    game.get_grid().settle_tetramino()
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
        #print(game.grid.available_tetraminos[game.grid.active_tetramino].get_str_grid())
        print(game.grid.active.get_str_grid())
    except:
        print("No tetramino is available")

# test 15-17
def rotate_tetramino_clockwise(game):
    #game.grid.available_tetraminos[game.grid.active_tetramino].clockwise()
    game.grid.active.clockwise()

# test 18-21
def print_newline(game):
    print()

# test 22-23
def print_game_status(game):
    print(game.get_grid_with_tetramino().get_str_matrix())
    #print(game.get_grid().get_str_matrix())

# test 24-29, 39
# def move_left(game):
#     if game.grid.coor['x_axis'] > 0:
#         game.grid.clear_tetramino()
#         game.grid.coor['x_axis'] -= 1

def move_left(game):
    #tetra = game.grid.available_tetraminos[game.grid.active_tetramino]
    tetra = game.grid.active
    game.grid.clear_tetramino()
    if game.grid.coor['x_axis'] > 0:
        if not game.grid.check_collisions(game.grid.coor['x_axis'] - 1, game.grid.coor['y_axis']):
            game.grid.coor['x_axis'] -= 1
    elif game.grid.coor['x_axis'] == 0:
        tetra.shift_left()


# test 30, 33
# def move_right(game):
#     tetra = game.grid.available_tetraminos[game.grid.active_tetramino]
#     game.grid.clear_tetramino()
#     if game.grid.coor['x_axis'] < game.grid.cols - tetra.get_width():
#         game.grid.coor['x_axis'] += 1
#     elif game.grid.coor['x_axis'] == game.grid.cols - tetra.get_width():
#         tetra.shift_right()

# def move_right2(game):
#     tetra = game.grid.available_tetraminos[game.grid.active_tetramino]
#     game.grid.clear_tetramino()
#     if game.grid.coor['x_axis'] < game.grid.cols - tetra.get_width():
#         game.grid.coor['x_axis'] += 1
#         if game.check_collisions(game.grid.coor['x_axis'],game.grid.coor['y_axis']):
#             game.grid.coor['y_axis'] -= 1
#             game.get_grid().settle_tetramino()
#     elif game.grid.coor['x_axis'] == game.grid.cols - tetra.get_width():
#         tetra.shift_right()

def move_right(game):
    #tetra = game.grid.available_tetraminos[game.grid.active_tetramino]
    tetra = game.grid.active
    game.grid.clear_tetramino()
    if game.grid.coor['x_axis'] < game.grid.cols - tetra.get_width():
        if not game.grid.check_collisions(1 + game.grid.coor['x_axis'], game.grid.coor['y_axis']):
            #game.get_grid().settle_tetramino()
            game.grid.coor['x_axis'] += 1
    elif game.grid.coor['x_axis'] == game.grid.cols - tetra.get_width():
        tetra.shift_right()

# test 34
def rotate_tetramino_anticlockwise(game):
    #game.grid.available_tetraminos[game.grid.active_tetramino].anticlockwise()
    game.grid.active.anticlockwise()

# test 35
# def move_down(game):
#     tetra = game.grid.available_tetraminos[game.grid.active_tetramino]
#     game.grid.clear_tetramino()
#     if game.grid.coor['y_axis'] < game.grid.rows - tetra.get_hight():
#         game.grid.coor['y_axis'] += 1
#         if game.check_collisions():
#             game.grid.coor['y_axis'] -= 1
#             game.get_grid().settle_tetramino()
#             return False
#         return True
#     elif game.grid.coor['y_axis'] == game.grid.rows - tetra.get_hight():
#         tetra.shift_down()
#         return True
#     return False

# def move_down(game):
#     tetra = game.grid.available_tetraminos[game.grid.active_tetramino]
#     game.grid.clear_tetramino()
#     game.grid.coor['y_axis'] += 1
#     if game.grid.coor['y_axis'] < game.grid.rows - tetra.get_hight():
#         if game.grid.check_collisions():
#             game.grid.coor['y_axis'] -= 1
#             game.get_grid().settle_tetramino()
#             return False
#         return True
#     elif game.grid.coor['y_axis'] == game.grid.rows - tetra.get_hight():
#         if game.grid.check_collisions():
#             game.grid.coor['y_axis'] -= 1
#             game.get_grid().settle_tetramino()
#             return False
#         else:
#             #game.grid.coor['y_axis'] -= 1 # must be here
#             #tetra.shift_down()
#             return True
#     else:
#         game.grid.coor['y_axis'] -= 1
#         tetra.shift_down()
#         return True
#     return False

def move_down(game):
    #tetra = game.grid.available_tetraminos[game.grid.active_tetramino]
    tetra = game.grid.active
    game.grid.clear_tetramino()
    if game.grid.coor['y_axis'] < game.grid.rows - tetra.get_hight():
        if game.grid.check_collisions(game.grid.coor['x_axis'], 1+game.grid.coor['y_axis']):
            game.get_grid().settle_tetramino()
            return False
        game.grid.coor['y_axis'] += 1
        return True
    elif game.grid.coor['y_axis'] == game.grid.rows - tetra.get_hight():
        tetra.shift_down()
        if game.grid.check_collisions(game.grid.coor['x_axis'], game.grid.coor['y_axis']):
            tetra.shift_up()
            game.get_grid().settle_tetramino()
            return False
        else:
            #game.grid.coor['y_axis'] -= 1 # must be here
            #tetra.shift_down()
            return True
    else:
        game.get_grid().settle_tetramino()


# test 36-38
# def move_to_floor(game):
#     tetra = game.grid.available_tetraminos[game.grid.active_tetramino]
#     tetra.shift_down()
#     game.grid.clear_tetramino()
#     for item in range(game.grid.rows - tetra.get_hight() + 1):
#         game.grid.coor['y_axis'] = item
#         if game.check_collisions():
#             game.grid.coor['y_axis'] -= 1
#             game.get_grid().settle_tetramino()
#             break
#     game.get_grid().settle_tetramino()

def move_to_floor(game):
    #tetra = game.grid.available_tetraminos[game.grid.active_tetramino]
    tetra = game.grid.active
    tetra.shift_down()
    game.grid.clear_tetramino()
    for item in range(game.grid.rows - tetra.get_hight() + 1):
        game.grid.coor['y_axis'] = item
        if not move_down(game):
            break
    game.get_grid().settle_tetramino()
