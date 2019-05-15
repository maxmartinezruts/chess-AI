import pygame
import numpy as np
import time
import pieces as pcs
import chess
board = chess.Board()

# Convert coordinates form cartesian to screen coordinates (used to draw in pygame screen)
def cartesian_to_screen(car_pos):
    factor = 1
    screen_pos = np.array([center[0]*factor+car_pos[0],center[1]*factor+car_pos[1]])/factor
    screen_pos = screen_pos.astype(int)
    return screen_pos

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
# Screen parameters
width = 800
height = 800
center = np.array([width/2, height/2])
screen = pygame.display.set_mode((width, height))

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255,255, 0)
black = (0,0, 0)
black_soft = (181,136,96)
white_soft = (240,217,178)


pos_distribution = np.linspace(-350,350,8)
grid_distribution = np.zeros((8,8,2))
for i in range(0,8):
    for j in range(0,8):
        grid_distribution[j,i] = np.array([pos_distribution[i],pos_distribution[j]])
print(grid_distribution.shape)
board =  np.ndarray((8,8), dtype=np.object)
boards_squares = np.ndarray((8,8), dtype=np.object)
pieces = []

for i in range(0,8):
    pieces.append(pcs.Pawn('b', (1,i)))

for i in range(0,8):
    pieces.append(pcs.Pawn('w', (6, i)))
# pieces[3].pos = (3,3)
# pieces[9].pos = (5,7)


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
pieces.append(pcs.Queen('w',(7,4)))

pieces.append(pcs.King('b',(0,4)))
pieces.append(pcs.King('w',(7,3)))




for piece in pieces:
    board[piece.pos] = piece

for i in range(0,8):
    for j in range(0,8):
        if (i + j) % 2 == 0:
            boards_squares[j,i] = (pygame.Rect(cartesian_to_screen(grid_distribution[j,i])[0] - 50,
                    cartesian_to_screen(grid_distribution[j, i])[1] - 50, 100, 100), white_soft)
        else:
            boards_squares[j,i] = (pygame.Rect(cartesian_to_screen(grid_distribution[j, i])[0] - 50,
                                                cartesian_to_screen(grid_distribution[j, i])[1] - 50, 100, 100),
                                    black_soft)

#
# board[7,4].pos = (4,3)
# board[4,3] = board[7,4]
# board[7,4] = None
#
# board[7,6].pos = (3,3)
# board[3,3] = board[7,6]
# board[7,6] = None
def min_search(bd, lv, bds, max_val):
    max_val = float(max_val)
    bds = list(bds)
    bds.append(bd)
    if lv ==0:
        val = get_score(bd)
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
        val = get_score(bd)
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

def draw(bd):
    # pygame.event.get()
    screen.fill((0, 0, 0))
    for i in range(0, 8):
        for j in range(0, 8):

            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, boards_squares[i, j][1], boards_squares[i, j][0])
            else:
                pygame.draw.rect(screen, boards_squares[i, j][1], boards_squares[i, j][0])
    for i in range(0, 8):
        for j in range(0, 8):
            piece = bd[i, j]
            if piece != None:
                screen.blit(pygame.transform.scale(pygame.image.load(piece.image), (80, 80)),
                            cartesian_to_screen(grid_distribution[(i, j)] - np.array([40, 40])))
    pygame.display.flip()


def wt(bd):
    wait = True
    piece_drag = 0
    start = ()
    end = ()
    while wait:

        for event in pygame.event.get():

            for i in range(0, 8):
                for j in range(0, 8):
                    if (i + j) % 2 == 1:
                        boards_squares[i, j] = (boards_squares[i, j][0], black_soft)
                    if (i + j) % 2 == 0:
                        boards_squares[i, j] = (boards_squares[i, j][0], white_soft)
            if event.type == pygame.MOUSEMOTION:
                # Record mouse position
                mouse_pos = event.pos

                for i in range(0, 8):
                    for j in range(0, 8):
                        if boards_squares[i, j][0].collidepoint(mouse_pos):
                            if board[i, j] != None:
                                if (i+j)%2==1:
                                    boards_squares[i, j] = (boards_squares[i, j][0], black_soft)
                                    moves = board[i,j].moves(board, (i,j))
                                if (i + j) % 2 == 0:
                                    boards_squares[i, j] = (boards_squares[i, j][0], white_soft)
                                    moves = board[i, j].moves(board, (i, j))
                                for move in moves:
                                    for k in range(0,8):
                                        for l in range(0,8):
                                            if move[k,l] == board[i,j]:
                                                if (k+l)%2==0:
                                                    boards_squares[k,l] = (boards_squares[k,l][0], (190, 167, 128))
                                                else:
                                                    boards_squares[k,l] = (boards_squares[k,l][0], (131, 86, 46))

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Record mouse position
                mouse_pos = event.pos
                for i in range(0, 8):
                    for j in range(0, 8):
                        if board[i, j] != None and boards_squares[i, j][0].collidepoint(mouse_pos):
                            start = (i,j)
                            print('start')
            if event.type == pygame.MOUSEBUTTONUP:
                # Record mouse position
                mouse_pos = event.pos
                for i in range(0, 8):
                    for j in range(0, 8):
                        if boards_squares[i, j][0].collidepoint(mouse_pos):
                            if start != ():
                                end = (i,j)
                                wait = False

        draw(bd)
    board[end]= board[start]
    board[start] = None
    draw(bd)


while True:


    res = min_search(board, 4, [], -9999)
    print(res[0], 'w')
    board = res[1][1]
    wt(board)






