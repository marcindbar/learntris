from task import *

execute = dict({'q':quit_game, 'p':print_game_grid, 'g':set_game_grid,
                'c':clean_game_grid, '?s':print_game_score,
                '?n':print_game_cleand_lines, 's':update_score_table,
                'I':activate_tetramino,'Z':activate_tetramino,
                'O':activate_tetramino,'J':activate_tetramino,
                'S':activate_tetramino,'L':activate_tetramino,
                'T':activate_tetramino,'t':print_active_tetramino,
                ')':rotate_tetramino_clockwise,';':print_newline})
