"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1

    if count%2==0:
        return X
    if count%2==1:
        return O

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    availableActions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                availableActions.add((i, j))
    return availableActions

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Invalid.")

    else:
        newBoard = copy.deepcopy(board)
        newBoard[action[0]][action[1]] = player(board)
        return newBoard

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        xCounter = row.count(X)
        oCounter = row.count(O)
        if xCounter == 3:
            return X
        if oCounter == 3:
            return O

    columns = []
    for i in range(len(board)):
        column = [row[i] for row in board]
        columns.append(column)
    for j in columns:
        xCounter = j.count(X)
        oCounter = j.count(O)
        if xCounter == 3:
            return X
        if oCounter == 3:
            return O

    if (board[0][0] == O) and (board[1][1] == O) and (board[2][2] == O):
        return O
    if (board[0][0] == X) and (board[1][1] == X) and (board[2][2] == X):
        return X
    if (board[0][2] == O) and (board[1][1] == O) and (board[2][0] == O):
        return O
    if (board[0][2] == X) and (board[1][1] == X) and (board[2][0] == X):
        return X

    return None

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # If the game has a winner
    if (winner(board) != None):
        return True

    # If the game does not have a winner, but there is no further actions
    temp = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                temp.append(0)
    if len(temp) == 9:
        return True

    # If the game is not over yet
    else:
        return False

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """


    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0

    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None



    maxv = float("-inf")
    minv = float("inf")
    if player(board)==X:
        return maxValuef(board, maxv, minv)[1]
    if player(board)==O:
        return minValuef(board, maxv, minv)[1]

    # raise NotImplementedError


def maxValuef(board, maxValue, minValue):
    if terminal(board):
        return [utility(board), None]
    move = None
    v = float("-inf")
    for action in actions(board):
        test = minValuef(result(board, action), maxValue, minValue)[0]
        maxValue = max(maxValue, test)
        if v<test:
            v = test
            move = action
        if minValue <= maxValue:
            break
    return [v, move]

def minValuef(board, maxValue, minValue):
    if terminal(board):
        return [utility(board), None]
    move = None
    v = float("inf")
    for action in actions(board):
        test = maxValuef(result(board, action), maxValue, minValue)[0]
        minValue = min(minValue, test)
        if test < v:
            v = test
            move = action
        if minValue <= maxValue:
            break
    return [v, move]
