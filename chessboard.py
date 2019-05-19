import pygame
import numpy as np
import time
import pieces as pcs
import math
import chess
import drawing as dr

def get_score(board):
    score = 0
    for i in range(0,8):
        for j in range(0,8):
            if board[i,j] != None:
                score+= board[i,j].positining_score[i,j]
    score += np.sum(get_numerical(board))
    return score


def get_val(pos, board):
    if 0 <= pos[0] < 8 and 0<=pos[1]<8:
        if board[pos] == None:
            return 0
        else:
            return board[pos].value
    else:
        return None

def get_numerical(board):
    num_board = np.zeros((8,8))
    for i in range(0,8):
        for j in range(0,8):
            num_board[i,j] = get_val((i,j),board)
    return num_board

pieces = []

def initialize_board():
    board = np.ndarray((8, 8), dtype=np.object)

    for i in range(0,8):
        pieces.append(pcs.Pawn('b', (1,i)))

    for i in range(0,8):
        pieces.append(pcs.Pawn('w', (6, i)))

    pieces.append(pcs.Beeshop('b',(0,2)))
    pieces.append(pcs.Beeshop('b',(0,5)))
    pieces.append(pcs.Beeshop('w',(7,2)))
    pieces.append(pcs.Beeshop('w',(7,5)))

    pieces.append(pcs.Knight('b',(0,1)))
    pieces.append(pcs.Knight('b',(0,6)))
    pieces.append(pcs.Knight('w',(7,1)))
    pieces.append(pcs.Knight('w',(7,6)))

    pieces.append(pcs.Rook('b',(0,0)))
    pieces.append(pcs.Rook('b',(0,7)))
    pieces.append(pcs.Rook('w',(7,0)))
    pieces.append(pcs.Rook('w',(7,7)))

    pieces.append(pcs.Queen('b',(0,3)))
    pieces.append(pcs.Queen('w',(7,3)))

    pieces.append(pcs.King('b',(0,4)))
    pieces.append(pcs.King('w',(7,4)))

    for piece in pieces:
        board[piece.pos] = piece


    return board, pieces



def wt(bd):
    wait = True
    start = ()
    end = ()
    while wait:

        for event in pygame.event.get():

            for i in range(0, 8):
                for j in range(0, 8):
                    if (i + j) % 2 == 1:
                        dr.boards_squares[i, j] = (dr.boards_squares[i, j][0], dr.black_soft)
                    if (i + j) % 2 == 0:
                        dr.boards_squares[i, j] = (dr.boards_squares[i, j][0], dr.white_soft)
            if event.type == pygame.MOUSEMOTION:
                # Record mouse position
                mouse_pos = event.pos

                for i in range(0, 8):
                    for j in range(0, 8):
                        if dr.boards_squares[i, j][0].collidepoint(mouse_pos):
                            if bd[i, j] != None:
                                if (i+j)%2==1:
                                    dr.boards_squares[i, j] = (dr.boards_squares[i, j][0], dr.black_soft)
                                    moves = bd[i,j].moves(bd, (i,j))
                                if (i + j) % 2 == 0:
                                    dr.boards_squares[i, j] = (dr.boards_squares[i, j][0], dr.white_soft)
                                    moves = bd[i, j].moves(bd, (i, j))
                                for move in moves:
                                    for k in range(0,8):
                                        for l in range(0,8):
                                            if move[k,l] == bd[i,j]:
                                                if (k+l)%2==0:
                                                    dr.boards_squares[k,l] = (dr.boards_squares[k,l][0], (190, 167, 128))
                                                else:
                                                    dr.boards_squares[k,l] = (dr.boards_squares[k,l][0], (131, 86, 46))

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Record mouse position
                mouse_pos = event.pos
                for i in range(0, 8):
                    for j in range(0, 8):
                        if bd[i, j] != None and dr.boards_squares[i, j][0].collidepoint(mouse_pos):
                            start = (i,j)
                            print('start')
            if event.type == pygame.MOUSEBUTTONUP:
                # Record mouse position
                mouse_pos = event.pos
                for i in range(0, 8):
                    for j in range(0, 8):
                        if dr.boards_squares[i, j][0].collidepoint(mouse_pos):
                            if start != ():
                                end = (i,j)
                                wait = False
        dr.draw(bd)
    bd[end]= bd[start]
    bd[start] = None
    return bd





