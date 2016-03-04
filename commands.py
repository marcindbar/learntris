from task import *

execute = dict({'q':quit_game, 'p':print_game_grid, 'g':set_game_grid,
                'c':clean_game_grid, '?s':print_game_score,
                '?n':print_game_cleand_lines, 's':update_score_table,
                'I':activate_tetramino,'Z':activate_tetramino,
                'O':activate_tetramino,'J':activate_tetramino,
                'S':activate_tetramino,'L':activate_tetramino,
                'T':activate_tetramino,'t':print_active_tetramino,
                ')':rotate_tetramino_clockwise,';':print_newline,
                '(':rotate_tetramino_anticlockwise,'P':print_game_status,
                '<':move_left,'>':move_right,'v':move_down,
                'V':move_to_floor,'@':set_title_screen,'!':set_start_game,})
