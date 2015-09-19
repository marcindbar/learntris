#!/usr/bin/env python3
# tetris.py version 0.1

def print_empty_matrix():
    matrix = (". " * 10 + '\n') * 22
    print(matrix)

def print_matrix():
    matrix = """. . . . . . . . . .
    . . . . . . . . . .
    . . . . . . . . . .
    . . . . . . . . . .
    m m m m m m m m m m
    b b b b b b b b b b
    c c c c c c c c c c
    g g g g g g g g g g
    y y y y y y y y y y
    o o o o o o o o o o
    r r r r r r r r r r
    . . . . . . . . . .
    . . . . . . . . . .
    . . . . . . . . . .
    . . . . . . . . . .
    c . . . . . . . . .
    c . . . . . . . . .
    c . . . . g . . . .
    c . . o . g g . . .
    . . . o . b g . . .
    . m r r o o b y y .
    m m m r r b b y y ."""
    print(matrix)

if __name__ == "__main__":

    answer = input()
    # test 2
    if answer == 'p':
        print_empty_matrix()

    # test 3
    if answer == 'g':
        print_matrix()
