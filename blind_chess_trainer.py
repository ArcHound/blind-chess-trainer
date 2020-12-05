#!/usr/bin/env python3

from random import choice
from random import randint
import re

def choose_piece():
    pieces = ['wpawn', 'bpawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    return choice(pieces)


def generate_square(is_pawn):
    if is_pawn == False:
        f = randint(1,8)
        r = randint(1,8)
    else:
        f = randint(1,8)
        r = randint(2,7)
    return (f,r)

def print_square(square):
    s = chr(96+square[0])+str(square[1])
    return s

def get_answer():
    answer_syntax = False
    squares = []
    while answer_syntax == False:
        answer = input('List all valid moves:')
        squares = [x for x in re.split("\s|[,;]", answer) if x != '']
        answer_syntax = True
        for s in squares:
            if len(s) != 2:
                answer_syntax = False
            elif s[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                answer_syntax = False
            elif s[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
                answer_syntax = False
            if answer_syntax == False:
                print('Invalid square: '+s)
                print('Separate squares (a1, b6) with spaces or commas')
                break
    return squares

def w_pawn_moves(square):
    squares = [(square[0], square[1]+1)]
    if square[1] == 2:
        squares.append((square[0], square[1]+2))
    return squares

def b_pawn_moves(square):
    squares = [(square[0], square[1]-1)]
    if square[1] == 7:
        squares.append((square[0], square[1]-2))
    return squares

def bishop_moves(square):
    squares = []
    for i in range(1,8):
        if square[0]+i <= 8 and square[1]+i <= 8:
            squares.append((square[0]+i, square[1]+i))
        if square[0]-i >= 1 and square[1]+i <= 8:
            squares.append((square[0]-i, square[1]+i))
        if square[0]+i <= 8 and square[1]-i >= 1:
            squares.append((square[0]+i, square[1]-i))
        if square[0]-i >= 1 and square[1]-i >= 1:
            squares.append((square[0]-i, square[1]-i))
    return squares

def rook_moves(square):
    squares = []
    for i in range(1,8):
        if square[0]+i <= 8:
            squares.append((square[0]+i, square[1]))
        if square[0]-i >= 1:
            squares.append((square[0]-i, square[1]))
        if square[1]-i >= 1:
            squares.append((square[0], square[1]-i))
        if square[1]+i <= 8:
            squares.append((square[0], square[1]+i))
    return squares

def queen_moves(square):
    squares = rook_moves(square)+bishop_moves(square)
    return square

def king_moves(square):
    squares = []
    if square[0]+1 <= 8 and square[1]+1 <= 8:
        squares.append((square[0]+1, square[1]+1))
    if square[0]-1 >= 1 and square[1]+1 <= 8:
        squares.append((square[0]-1, square[1]+1))
    if square[0]+1 <= 8 and square[1]-1 >= 1:
        squares.append((square[0]+1, square[1]-1))
    if square[0]-1 >= 1 and square[1]-1 >= 1:
        squares.append((square[0]-1, square[1]-1))
    if square[0]+1 <= 8:
        squares.append((square[0]+1, square[1]))
    if square[0]-1 >= 1:
        squares.append((square[0]-1, square[1]))
    if square[1]-1 >= 1:
        squares.append((square[0], square[1]-1))
    if square[1]+1 <= 8:
        squares.append((square[0], square[1]+1))
    return squares

def knight_moves(square):
    squares = []
    if square[0]+1 <= 8 and square[1]+2 <= 8:
        squares.append((square[0]+1, square[1]+2))
    if square[0]+2 <= 8 and square[1]+1 <= 8:
        squares.append((square[0]+2, square[1]+1))
    if square[0]-1 >= 1 and square[1]+2 <= 8:
        squares.append((square[0]-1, square[1]+2))
    if square[0]-2 >= 1 and square[1]+1 <= 8:
        squares.append((square[0]-2, square[1]+1))
    if square[0]+1 <= 8 and square[1]-2 >= 1:
        squares.append((square[0]+1, square[1]-2))
    if square[0]+2 <= 8 and square[1]-1 >= 1:
        squares.append((square[0]+2, square[1]-1))
    if square[0]-1 >= 1 and square[1]-2 >= 1:
        squares.append((square[0]-1, square[1]-2))
    if square[0]-2 >= 1 and square[1]-1 >= 1:
        squares.append((square[0]-2, square[1]-1))
    return squares

def generate_moves(piece, starting_square):
    pieces = {'wpawn': w_pawn_moves, 'bpawn': b_pawn_moves, 'knight': knight_moves, 'bishop': bishop_moves, 'rook': rook_moves, 'queen': queen_moves, 'king': king_moves}
    return pieces[piece](starting_square)

def verify_answer(piece, starting_square, answer):
    correct_answer = generate_moves(piece, starting_square)
    missed = [print_square(x) for x in correct_answer if print_square(x) not in answer]
    wrong = [x for x in answer if x not in [print_square(y) for y in correct_answer]]
    is_correct = False
    if missed == [] and wrong == []:
        is_correct = True
    return is_correct, missed, wrong

def main():
    piece = choose_piece()
    is_pawn = False
    if piece == 'wpawn' or piece == 'bpawn':
        is_pawn = True
    standing_square = generate_square(is_pawn)
    print(piece+' '+print_square(standing_square))
    answer = get_answer()
    is_correct, missed, wrong = verify_answer(piece, standing_square, answer)
    if is_correct:
        print('Good job!')
    else:
        if missed != []:
            print('Too bad. You missed: '+', '.join(missed))
        if wrong != []:
            print("Oh no. You can't reach these: "+', '.join(wrong))

main()

