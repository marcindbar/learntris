#!/usr/bin/env python3
# tetris.py version 0.1

def print_matrix():
    matrix = (". " * 10 + '\n') * 22
    print(matrix if input() == 'p' else "")

if __name__ == "__main__":
    print_matrix()
