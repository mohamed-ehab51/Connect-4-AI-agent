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

def minimax(board, depth,is_maximizing, first_time=True):
    result = check_winner(board)
    if depth==0 or  result == 4 or result == -4 or result==-1:
        return result,1

    if is_maximizing:
        final_score = -math.inf
        for i in range(0, 6):
            for j in range(0, 7):
                if board[i][j] == '-':
                    if (i == 5) or (i != 5 and board[i + 1][j] != '-'):
                            board[i][j] = 'O'
                            score = minimax(board, depth-1,False, False)
                            board[i][j] = '-'
                            if score[0] > final_score:
                                final_score = score[0]
                                print("jj,", i, ",", j, ":", score[0])

                                final_i, final_j = i, j

        if first_time:
            board[final_i][final_j] = 'O'
        return final_score,final_j
    else:
        final_score1 = math.inf
        final_i, final_j = None, None
        for i in range(0, 6):
            for j in range(0, 7):
                if board[i][j] == '-':
                    if (i == 5) or (i != 5 and board[i + 1][j] != '-'):
                        board[i][j] = 'X'
                        score1 = minimax(board, depth-1,True, False)
                        board[i][j] = '-'
                        if score1[0] < final_score1:
                            final_score1 = score1[0]
                            print("j5,", i, ",", j, ":", score1[0])
                            final_i, final_j = i, j


        if first_time:
            board[final_i][final_j] = 'O'
        return final_score1,final_j
      
def prun_minimax(board, depth,alpha, beta,is_maximizing, first_time=True):
    result = check_winner(board)
    if depth==0 or  result == 4 or result == -4 or result==-1:
        return result,1

    if is_maximizing:
        final_score = -math.inf
        for i in range(0, 6):
            for j in range(0, 7):
                if board[i][j] == '-':
                    if (i == 5) or (i != 5 and board[i + 1][j] != '-'):
                            board[i][j] = 'O'
                            score = prun_minimax(board, depth-1,alpha, beta,False, False)
                            board[i][j] = '-'
                            if score[0] > final_score:
                                final_score = score[0]
                                print("jj,", i, ",", j, ":", score[0])
                                final_i, final_j = i, j
                            alpha = max(alpha, final_score)
                            if alpha >= beta:
                                break

        if first_time:
            board[final_i][final_j] = 'O'
        return final_score,final_j
    else:
        final_score1 = math.inf
        final_i, final_j = None, None
        for i in range(0, 6):
            for j in range(0, 7):
                if board[i][j] == '-':
                    if (i == 5) or (i != 5 and board[i + 1][j] != '-'):
                        board[i][j] = 'X'
                        score1 = prun_minimax(board, depth-1,alpha, beta,True, False)
                        board[i][j] = '-'
                        if score1[0] < final_score1:
                            final_score1 = score1[0]
                            print("j5,", i, ",", j, ":", score1[0])
                            final_i, final_j = i, j
                        beta = min(beta, final_score1)
                        if alpha >= beta:
                              break

        if first_time:
            board[final_i][final_j] = 'O'
        return final_score1,final_j
