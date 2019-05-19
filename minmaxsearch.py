# Author:   Max Martinez Ruts
# Creation: 2019

import chessboard as cb
import numpy as np

def min_search(bd, lv, bds, max_val):
    max_val = float(max_val)
    bds = list(bds)
    bds.append(bd)
    if lv ==0:
        val = cb.get_score(bd)
        return [val, bds]
    else:
        boards = []
        for j in range(0, 8):
            for k in range(0, 8):
                piece = bd[j, k]
                if piece != None and piece.color == 'w':
                    boards += piece.moves(bd, (j, k))
        sc = []
        ss = []
        min_val = 9999
        for board in boards:
            e = max_search(board, lv - 1, bds, min_val)
            sc.append(e)
            ss.append(e[0])
            if e[0] < min_val:
                min_val = e[0]
            if e[0] < max_val:
                break
        bds = sc[np.argmin(ss)][1]
        return [np.min(ss), bds]

def max_search(bd, lv, bds, min_val):
    min_val = float(min_val)
    bds = list(bds)
    bds.append(bd)
    if lv == 0:
        val = cb.get_score(bd)
        # draw(bd)
        return [val, bds]
    else:
        boards = []
        for j in range(0, 8):
            for k in range(0, 8):
                piece = bd[j, k]
                if piece != None and piece.color == 'b':
                    boards += piece.moves(bd, (j, k))
        sc = []
        ss = []
        max_val = -9999
        for board in boards:
            e = min_search(board, lv - 1, bds, max_val)
            sc.append(e)
            ss.append(e[0])
            if e[0] > max_val:
                max_val = e[0]
            if e[0] > min_val:
                break
        bds = sc[np.argmax(ss)][1]

        return [np.max(ss), bds]
