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


def equivelant_not_empty(x, y, z,w):
    if x == y and x == z and x == w and x != '-':
        return True
    return False
#x x x -

def equivelant_not_empty2(x, y, z, w):
    if x == y and x == z and w == '-' and x != '-':
        return True
    return False

#x x - x
def equivelant_not_empty3(x, y, z, w):
    if x == y and x == w and z == '-' and x != '-':
        return True
    return False
#x - x x
def equivelant_not_empty4(x, y, z, w):
    if x == z and x == w and y == '-' and x != '-':
        return True
    return False
#- x x x

def equivelant_not_empty5(x, y, z, w):
    if y == z and y == w and x == '-' and y != '-':
        return True
    return False
def equivelant_not_empty6(x, y, z, w):
    if x == y and z == '-' and w == '-' and x != '-':
        return True
    return False


def equivelant_not_empty7(x, y, z, w):
    if z == w and x == '-' and y == '-' and z != '-':
        return True
    return False


# x-x-
# -x-x
def equivelant_not_empty8(x, y, z, w):
    if x == z and y == '-' and w == '-' and x != '-':
        return True
    return False


def equivelant_not_empty9(x, y, z, w):
    if y == w and x == '-' and z == '-' and y != '-':
        return True
    return False


# x--x
def equivelant_not_empty10(x, y, z, w):
    if x == w and y == '-' and z == '-' and x != '-':
        return True
    return False


def equivelant_not_empty11(x, y, z, w):
    if y == z and x == '-' and w == '-' and y != '-':
        return True
    return False

def check_winner(board):


   for index in range(0, 4):
            for row in range(0, 6):
                first = index
                second = first + 1
                third = first + 2
                forth = first + 3
                if equivelant_not_empty(board[row][first], board[row][second], board[row][third], board[row][forth]):
                    return 4 if board[row][index] == 'O' else -4
        for index in range(0, 4):
            for row in range(0, 6):
                first = index
                second = first + 1
                third = first + 2
                forth = first + 3
                if equivelant_not_empty2(board[row][first], board[row][second], board[row][third], board[row][forth]):
                    return 2 if board[row][index] == 'O' else -20

        for index in range(0, 4):
            for row in range(0, 6):
                first = index
                second = first + 1
                third = first + 2
                forth = first + 3
                if equivelant_not_empty3(board[row][first], board[row][second], board[row][third], board[row][forth]):
                    return 2 if board[row][index] == 'O' else -20
        for index in range(0, 4):
            for row in range(0, 6):
                first = index
                second = first + 1
                third = first + 2
                forth = first + 3
                if equivelant_not_empty4(board[row][first], board[row][second], board[row][third], board[row][forth]):
                    return 2 if board[row][index] == 'O' else -20

        for index in range(0, 4):
            for row in range(0, 6):
                first = index
                second = first + 1
                third = first + 2
                forth = first + 3
                if equivelant_not_empty5(board[row][first], board[row][second], board[row][third], board[row][forth]):
                    return 2 if board[row][index] == 'O' else -20
           for index in range(0, 4):
        for row in range(0, 6):
            first = index
            second = first + 1
            third = first + 2
            forth = first + 3
            if equivelant_not_empty6(board[row][first], board[row][second], board[row][third], board[row][forth]):
                return 1 if board[row][index] == 'O' else -10

    for index in range(0, 4):
        for row in range(0, 6):
            first = index
            second = first + 1
            third = first + 2
            forth = first + 3
            if equivelant_not_empty7(board[row][first], board[row][second], board[row][third], board[row][forth]):
                return 1 if board[row][index] == 'O' else -10

    for index in range(0, 4):
        for row in range(0, 6):
            first = index
            second = first + 1
            third = first + 2
            forth = first + 3
            if equivelant_not_empty8(board[row][first], board[row][second], board[row][third], board[row][forth]):
                return 1 if board[row][index] == 'O' else -10

    for index in range(0, 4):
        for row in range(0, 6):
            first = index
            second = first + 1
            third = first + 2
            forth = first + 3
            if equivelant_not_empty9(board[row][first], board[row][second], board[row][third], board[row][forth]):
                return 1 if board[row][index] == 'O' else -10
    for index in range(0, 4):
        for row in range(0, 6):
            first = index
            second = first + 1
            third = first + 2
            forth = first + 3
            if equivelant_not_empty10(board[row][first], board[row][second], board[row][third], board[row][forth]):
                return 1 if board[row][index] == 'O' else -10
    for index in range(0, 4):
        for row in range(0, 6):
            first = index
            second = first + 1
            third = first + 2
            forth = first + 3
            if equivelant_not_empty11(board[row][first], board[row][second], board[row][third], board[row][forth]):
                return 1 if board[row][index] == 'O' else -10
      ## column

        for index in range(0, 7):
            for row in range(0, 3):
                first = row
                second = first + 1
                third = first + 2
                forth = first + 3
                if equivelant_not_empty(board[first][index], board[second][index], board[third][index],
                                        board[forth][index]):
                    return 4 if board[row][index] == 'O' else -4
        for index in range(0, 7):
            for row in range(0, 3):
                first = row
                second = first + 1
                third = first + 2
                forth = first + 3
                if equivelant_not_empty2(board[first][index], board[second][index], board[third][index],
                                        board[forth][index]):
                    return 2 if board[row][index] == 'O' else -20
        for index in range(0, 7):
            for row in range(0, 3):
                first = row
                second = first + 1
                third = first + 2
                forth = first + 3
                if equivelant_not_empty5(board[first][index], board[second][index], board[third][index],
                                        board[forth][index]):
                    return 2 if board[row][index] == 'O' else -20
      for index in range(0, 7):
         for row in range(0, 3):
            first = row
            second = first + 1
            third = first + 2
            forth = first + 3
            if equivelant_not_empty6(board[first][index], board[second][index], board[third][index],
                                     board[forth][index]):
                return 1 if board[row][index] == 'O' else -10

    for index in range(0, 7):
        for row in range(0, 3):
            first = row
            second = first + 1
            third = first + 2
            forth = first + 3
            if equivelant_not_empty7(board[first][index], board[second][index], board[third][index],
                                     board[forth][index]):
                return 1 if board[row][index] == 'O' else -10         
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
                return 4 if board[first][first2] == 'O' else -4
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
            if equivelant_not_empty2(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 2 if board[first][first2] == 'O' else -20
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
            if equivelant_not_empty3(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 2 if board[first][first2] == 'O' else -20

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
            if equivelant_not_empty4(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 2 if board[first][first2] == 'O' else -20
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
            if equivelant_not_empty5(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 2 if board[first][first2] == 'O' else -20
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
            if equivelant_not_empty6(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
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
            if equivelant_not_empty7(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
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
            if equivelant_not_empty8(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10          

        ##mostafa
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
            if equivelant_not_empty9(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
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
            if equivelant_not_empty10(board[first][first2], board[second][second2], board[third][third2],
                                      board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
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
            if equivelant_not_empty11(board[first][first2], board[second][second2], board[third][third2],
                                      board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
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
                return 4 if board[first][first2] == 'O' else -4
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
            if equivelant_not_empty2(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 2 if board[first][first2] == 'O' else -20

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
            if equivelant_not_empty3(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 2 if board[first][first2] == 'O' else -20
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
            if equivelant_not_empty4(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 2 if board[first][first2] == 'O' else -20
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
            if equivelant_not_empty5(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 2 if board[first][first2] == 'O' else -20
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
            if equivelant_not_empty6(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
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
            if equivelant_not_empty7(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
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
            if equivelant_not_empty8(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
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
            if equivelant_not_empty9(board[first][first2], board[second][second2], board[third][third2],
                                     board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
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
            if equivelant_not_empty10(board[first][first2], board[second][second2], board[third][third2],
                                      board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
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
            if equivelant_not_empty11(board[first][first2], board[second][second2], board[third][third2],
                                      board[forth][forth2]):
                return 1 if board[first][first2] == 'O' else -10
    tie = True
    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == '-':
                tie = False
    if tie:
        return -1
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
a1 = []


def GUI(page: ft.Page):
    page.window_width = 585
    page.window_height = 530
    page.bgcolor = ft.colors.WHITE

    def star(e):
        if d.value != None and a.value != None:
            page.window_close()

    def diff(e):
        d.value = e.control.value

    global d
    d = ft.Text()

    def algo(e):
        a.value = e.control.value

    global a
    a = ft.Text()
    c1 = ft.Container(
        width=585,
        height=475,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.BLACK, ft.colors.DEEP_PURPLE_900],
        ),
        content=ft.Column([ft.Container(
            ft.Text(
                'Welcome in Connect 4 VS AI',
                size=32,
                weight=FontWeight.BOLD,
                color=ft.colors.WHITE,
            ), padding=ft.padding.only(0, 50, 0, 0), alignment=ft.alignment.center),
            ft.Row([ft.Column([ft.Container(
                ft.Text(
                    'Please choose the difficulty',
                    size=12,
                    weight=FontWeight.BOLD,
                    color=ft.colors.WHITE,
                ), padding=ft.padding.only(10, 30, 192, 0), alignment=ft.alignment.center),
                ft.Container(
                    content=ft.RadioGroup(content=ft.Column([
                        ft.Radio(value="easy", label="Easy"),
                        ft.Radio(value="hard", label="Hard")]), on_change=diff)
                    , )
            ]), ft.Column([ft.Container(
                ft.Text(
                    'Please choose the algorithm',
                    size=12,
                    weight=FontWeight.BOLD,
                    color=ft.colors.WHITE,
                ), padding=ft.padding.only(0, 25, 0, 0), alignment=ft.alignment.center),
                ft.Container(
                    content=ft.RadioGroup(content=ft.Column([
                        ft.Radio(value="minimax", label="Minimax"),
                        ft.Radio(value="alpha beta pruining", label="Alpha Beta Pruining"),
                    ]), on_change=algo)
                    , )
            ])]),
            ft.Container(content=ft.ElevatedButton("Start", on_click=star, bgcolor=ft.colors.WHITE),
                         alignment=ft.alignment.center,
                         padding=ft.padding.only(0, 100, 0, 0))])
    )
    page.add(c1)


countn = 0


def main():
    global countn
    board1 = Board()
    time.sleep(2)
    counter = 0
    game_end = False
    while not game_end:
        (board, game_end) = board1.get_game_grid()
        if counter == 0:
            r = 3
            counter = 1
        else:
            if d.value == "easy" and a.value == "minimax":
                result, r = minimax(board, 2, False)
            elif d.value == "hard" and a.value == "minimax":
                result, r = minimax(board, 5, False)
            elif d.value == "easy" and a.value == "alpha beta pruining":
                result, r = prun_minimax(board, 2, -math.inf, math.inf, False)
            elif d.value == "hard" and a.value == "alpha beta pruining":
                result, r = prun_minimax(board, 5, -math.inf, math.inf, False)
        board1.print_grid(board)
        board1.select_column(r)
        for i in range(len(board)):
            print(board[i])
        print('Number of nodes : ', len(a1))
        countn = countn + len(a1)
        a1.clear()
        time.sleep(2)
    print('total number of nodes : ', countn)


if __name__ == "__main__":
    ft.app(target=GUI)
    if d.value != None and a.value != None:
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("http://kevinshannon.com/connect4/")
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)
        element2 = driver.find_element(By.ID, "single")
        element2.click()
        main()
        driver.close()
