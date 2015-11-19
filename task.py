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
        game.set_active_tetramino(game.next_command)
    except KeyError as err:
        print(err)

# test 8-14 part2
def print_active_tetramino(game):
    try:
        print(game.available_tetraminos[game.active_tetramino].get_str_grid())
    except:
        print("No tetramino is available")