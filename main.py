import math
a1=[]
board = [    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ']
             ]

def equivelant_not_empty(x, y, z, w):
    if x == y and x == z and x == w and x != ' ':
        return True
    return False


def check_winner(board):
    for index in range(0, 4):
        for row in range(0, 6):
            first = index
            second = first + 1
            third = first + 2
            forth = first + 3
            if equivelant_not_empty(board[row][first], board[row][second], board[row][third],
                                    board[row][forth]):
                return 2 if board[row][index] == 'X' else -2
    for index in range(0, 7):
        for row in range(0, 3):
            first = row
            second = first + 1
            third = first + 2
            forth = first + 3
            if equivelant_not_empty(board[first][index], board[second][index], board[third][index],
                                    board[forth][index]):
                return 2 if board[row][index] == 'X' else -2
    for index in range(0, 4):
        for row in range(0, 3):
            first = row
            second = first + 1
            third = first + 2
            forth = first + 3
            first2 = index
            second2 = first2 + 1
            third2 = first2 + 2
            forth2 = first2 + 3
            if equivelant_not_empty(board[first][first2], board[second][second2], board[third][third2],
                                    board[forth][forth2]):
                return 2 if board[first][first2] == 'X' else -2
    for index in range(0, 4):
        for row in range(3, 6):
            first = row
            second = first - 1
            third = first - 2
            forth = first - 3
            first2 = index
            second2 = first2 + 1
            third2 = first2 + 2
            forth2 = first2 + 3
            if equivelant_not_empty(board[first][first2], board[second][second2], board[third][third2],
                                    board[forth][forth2]):
                return 2 if board[first][first2] == 'X' else -2

    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == ' ':
                return 1

    return 0
# my code part

def minimax(board, depth, is_maximizing, first_time=True):
    result = check_winner(board)
    if depth == 0 or result != 1:
        return result, 1, 1

    if is_maximizing:
        final_score = -math.inf
        for i in range(0, 6):
            for j in range(0, 7):
                if board[i][j] == ' ':
                    if (i == 5 and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 6)) or (
                            i != 5 and board[i + 1][j] != ' '):
                        board[i][j] = 'X'
                        scores = minimax(board, depth - 1, False, False)
                        score = scores[0]
                        board[i][j] = ' '
                        if score > final_score:
                            final_score = score
                            final_i, final_j = i, j
                        a1.append(final_score)

        if first_time:
            board[final_i][final_j] = 'O'
        return final_score, final_i, final_j
    else:
        final_score = math.inf
        final_i, final_j = None, None
        for i in range(0, 6):
            for j in range(0, 7):
                if board[i][j] == ' ':
                    if (i == 5 and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 6)) or (
                            i != 5 and board[i + 1][j] != ' '):
                        board[i][j] = 'O'
                        scores = minimax(board, depth - 1, True, False)
                        score = scores[0]
                        board[i][j] = ' '
                        if score < final_score:
                            final_score = score
                            final_i, final_j = i, j
                        a1.append(final_score)

        if first_time:
            board[final_i][final_j] = 'O'
        return final_score, final_i, final_j
