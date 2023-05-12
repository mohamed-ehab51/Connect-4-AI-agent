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