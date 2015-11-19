#!/usr/bin/env python3

'''
Code I wrote to pass the game's tests are in files:
tetris.py
commands_dict.py
game_elements
task_functions.py
tetraminos.txt
'''

from commands import execute
from game_elements import Cell, Matrix, Tetramino, Game


if __name__ == "__main__":
    game = Game()
    game.load_tetraminos('tetraminos.txt')

    while True:
        try:
            game.set_next_command()
            execute[game.next_command](game)
        except KeyError:
            continue
