"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # return [[EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]

    return [[X, X, EMPTY],
            [O, O, EMPTY],
            [EMPTY, O, X]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if not any(element for sublist in board for element in sublist):
        return X

    count_of_X = 0
    count_of_O = 0
    for row in board:
        count_of_X += row.count(X)
        count_of_O += row.count(O)
    if count_of_X > count_of_O:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    x = {(0,2), (1,2), (2,0)}
    print(x)
    return x


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    if board[action[0]][action[1]] != EMPTY:
        raise NameError('HiThere')('this action is not allowed in this board')
    
    result = board
    
    result[action[0]][action[1]] = player(board)

    return result
        
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError
    return (0,2)
