import numpy as np

A = np.ones((3,3))
a = (1,2)
print(A[a])

def get_val(pos, board):
    if 0 <= pos[0] < 8 and 0<=pos[1]<8:
        if board[pos] == None:
            return 0
        else:

            return board[pos].value
    else:
        return None

class Pawn:
    def __init__(self, color, pos):
        self.color = color
        if color == 'b':
            self.value = 10.0
            self.positining_score = np.array([
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
                [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
                [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
                [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
                [1.0, 1.0, 2.0, 3.0, 3.0, 1.0, 1.0, 1.0],
                [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
            )
        else:
            self.value = -10.0
            self.positining_score = np.array([
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
                [1.0, 1.0, 2.0, 3.0, 3.0, 1.0, 1.0, 1.0],
                [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
                [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
                [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
                [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
            )*-1
        self.pos = pos
        self.image = 'pawn'+color+'.png'

    def moves(self, board, pos):
        moves = []
        # Forward
        new_pos = (pos[0]+int(self.value/10),pos[1])
        val = get_val(new_pos,board)
        if val == 0:
            # Move
            new_board = np.array(list(board))
            new_board[pos] = None
            new_board[new_pos] = self
            moves.append(new_board)
            new_pos = (pos[0] + int(self.value/10)*2, pos[1])
            val = get_val(new_pos, board)
            if val == 0:
                # Move
                new_board = np.array(list(board))
                new_board[pos] = None
                new_board[new_pos] = self
                moves.append(new_board)

        new_pos = (pos[0] + int(self.value/10), pos[1]+1)
        val = get_val(new_pos, board)
        if val != None and val/self.value <0:
            # Move
            new_board = np.array(list(board))
            new_board[pos] = None
            new_board[new_pos] = self
            moves.append(new_board)
        new_pos = (pos[0] + int(self.value/10), pos[1] - 1)
        val = get_val(new_pos, board)
        if val != None and val / self.value < 0:
            # Move
            new_board = np.array(list(board))
            new_board[pos] = None
            new_board[new_pos] = self
            moves.append(new_board)
        return moves

class Beeshop:
    def __init__(self, color, pos):
        self.color = color
        if color == 'b':
            self.value = 30.0
            self.positining_score = np.array([
                [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
                [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
                [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
                [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
                [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
                [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
                [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
                [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]
            )
        else:
            self.value = -30.0
            self.positining_score = np.array([
                [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
                [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
                [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
                [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
                [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
                [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
                [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
                [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]
            )*-1

        self.pos = pos
        self.image = 'beeshop'+color + '.png'

    def moves(self, board, pos):
        moves = []
        # Forward
        for i in [-1,1]:
            for j in [-1,1]:
                k = 1
                new_pos = (pos[0] + k*i, pos[1] + k*j)
                value = get_val(new_pos, board)
                while value == 0:

                    new_board = np.array(list(board))
                    new_board[pos] = None
                    new_board[new_pos] = self
                    moves.append(new_board)
                    # print(pos,self.color,new_pos,k,i,j, value)

                    k+=1
                    new_pos = (pos[0] + k * i, pos[1] + k * j)
                    value = get_val(new_pos, board)
                if value != None and value/self.value < 0:
                    new_board = np.array(list(board))
                    new_board[pos] = None
                    new_board[new_pos] = self
                    moves.append(new_board)
                    # print(pos,self.color,new_pos,k,i,j, value)

        return moves

class Knight:
    def __init__(self, color, pos):
        self.color = color
        if color == 'b':
            self.value = 30.0
            self.positining_score = np.array([
                [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
                [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
                [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
                [-3.0, 0.5, 1.0, 2.0, 2.0, 1.0, 0.5, -3.0],
                [-3.0, 0.5, 1.0, 2.0, 2.0, 1.0, 0.5, -3.0],
                [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
                [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
                [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]
            )
        else:
            self.value = -30.0
            self.positining_score = np.array([
                [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
                [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
                [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
                [-3.0, 0.5, 1.0, 2.0, 2.0, 1.0, 0.5, -3.0],
                [-3.0, 0.5, 1.0, 2.0, 2.0, 1.0, 0.5, -3.0],
                [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
                [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
                [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]
            )*-1
        self.pos = pos
        self.image = 'knight'+color+'.png'


    def moves(self, board, pos):
        moves = []
        # Forward
        for move in [(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2)]:
            new_pos =  (move[0]+pos[0],move[1]+pos[1])
            value = get_val(new_pos, board)
            if value != None and value/self.value <= 0:

                new_board = np.array(list(board))
                new_board[pos] = None
                new_board[new_pos] = self
                moves.append(new_board)
                # print(pos,self.color,new_pos,value,move,'knight')
        return moves

class Rook:
    def __init__(self, color, pos):
        self.color = color
        if color == 'b':
            self.value = 50.0
            self.positining_score = np.array([
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
                [-0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.5],
                [-0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.5],
                [-0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.5],
                [-0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.5],
                [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
            )
        else:
            self.value = -50.0
            self.positining_score = np.array([
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
                [-0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.5],
                [-0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.5],
                [-0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.5],
                [-0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.5],
                [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
            ) * -1

        self.pos = pos
        self.image = 'rook'+color+'.png'

    def moves(self, board, pos):
        moves = []
        # Forward
        for move in [(-1,0),(1,0),(0,-1),(0,1)]:
            k = 1
            new_pos = (pos[0] + k * move[0], pos[1] + k * move[1])
            value = get_val(new_pos, board)
            while value == 0:
                new_board = np.array(list(board))
                new_board[pos] = None
                new_board[new_pos] = self
                moves.append(new_board)
                # print(pos, self.color, new_pos, k, value, 'rook')
                k += 1
                new_pos = (pos[0] + k * move[0], pos[1] + k * move[1])
                value = get_val(new_pos, board)
            if value != None and value / self.value < 0:
                new_board = np.array(list(board))
                new_board[pos] = None
                new_board[new_pos] = self
                moves.append(new_board)
                # print(pos, self.color, new_pos, k, value, 'rook')
        return moves

class Queen:
    def __init__(self, color, pos):
        self.color = color
        if color == 'b':
            self.value = 90.0
            self.positining_score = np.array([
                [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
                [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
                [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
                [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
                [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
                [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
                [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
                [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]
            )
        else:
            self.value = -90.0
            self.positining_score = np.array([
                [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
                [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
                [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
                [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
                [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
                [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
                [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
                [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]
            )*-1
        self.pos = pos
        self.image = 'queen'+color+'.png'


    def moves(self, board, pos):
        moves = []
        # Forward
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                k = 1
                new_pos = (pos[0] + k*i, pos[1] + k*j)
                value = get_val(new_pos, board)
                while value == 0:

                    new_board = np.array(list(board))
                    new_board[pos] = None
                    new_board[new_pos] = self
                    moves.append(new_board)
                    # print(pos,self.color,new_pos, value, 'Queen')

                    k+=1
                    new_pos = (pos[0] + k * i, pos[1] + k * j)
                    value = get_val(new_pos, board)
                if value != None and value/self.value < 0:
                    new_board = np.array(list(board))
                    new_board[pos] = None
                    new_board[new_pos] = self
                    moves.append(new_board)
                    # print(pos,self.color,new_pos,value, 'Queen')

        return moves

class King:
    def __init__(self, color, pos):
        self.color = color
        if color == 'b':
            self.value = 900.0
            self.positining_score = np.array([
                [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0],
                [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
                [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
                [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0]]
            )
        else:
            self.value = -900.0
            self.positining_score = np.array([
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
                [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
                [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
                [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]]
            )*-1
        self.pos = pos
        self.image = 'king'+color+'.png'

    def moves(self, board, pos):
        moves = []

        # Forward
        for move in [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]:
            new_pos =  (move[0]+pos[0],move[1]+pos[1])
            value = get_val(new_pos, board)
            if value != None and value/self.value <= 0:
                new_board = np.array(list(board))
                new_board[pos] = None
                new_board[new_pos] = self
                moves.append(new_board)
                # print(pos,self.color,new_pos,value,'king')
        return moves