# Author:   Max Martinez Ruts
# Creation: 2019

import time
import chessboard as cb
import drawing as dr
import minmaxsearch as mm

treeshape = [0,0,0,0,0]

board, pieces = cb.initialize_board()

while True:
    print(print(cb.get_numerical(board)))

    board  = cb.wt(board)
    dr.draw(board)

    start = time.time()
    res = mm.max_search(board, 3, [], 9999)
    print('Execution time: ', time.time()-start, ' Tree shape: ' ,treeshape)
    print(res[0], 'b')
    board = res[1][1]
    dr.draw(board)
    sc = cb.get_score(board)
    if sc < -500:
        print('White wins')
    if sc > 500:
        print('Black wins')
    print('score',cb.get_score(board))





