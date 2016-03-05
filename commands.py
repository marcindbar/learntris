from task import *

# game commands
execute = dict({

    # score
    '?s': print_game_score,
    's': update_score_table,

    # tetramino - printing
    't': print_active_tetramino,

    # tetramino - activating
    'I': activate_tetramino,
    'Z': activate_tetramino,
    'O': activate_tetramino,
    'J': activate_tetramino,
    'S': activate_tetramino,
    'L': activate_tetramino,
    'T': activate_tetramino,

    # tetramino - moving
    '<': move_left,
    '>': move_right,
    'v': move_down,
    'V': move_to_floor,
    ')': rotate_tetramino_clockwise,
    '(': rotate_tetramino_anticlockwise,

    # other
    'q': quit_game,
    'g': set_game_grid,
    'p': print_game_grid,
    'P': print_game_status,
    'c': clean_game_grid,
    ';': print_newline,
    '?n': print_game_cleand_lines,
    '@': set_title_screen,
    '!': set_start_game,

    })