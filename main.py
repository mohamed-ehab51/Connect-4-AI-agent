from flet_core import FontWeight
from board import Board
import time
import flet as ft
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
# GAME LINK
# http://kevinshannon.com/connect4/

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
                    return 40 if board[row][index] == 'O' else -40
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
                    return 40 if board[row][index] == 'O' else -40
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
                return 40 if board[first][first2] == 'O' else -40
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
                return 40 if board[first][first2] == 'O' else -40
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
    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == '-':
                return 1

    return 0
# my code part

def minimax(board, depth,is_maximizing, first_time=True):
    result = check_winner(board)
    if depth==0 or  result == 40 or result == -40 or result==-1:
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
                            final_i, final_j = i, j


        if first_time:
            board[final_i][final_j] = 'O'
        return final_score1,final_j
      
def prun_minimax(board, depth,alpha, beta,is_maximizing, first_time=True):
    result = check_winner(board)
    if depth==0 or  result == 40 or result == -40 or result==-1:
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
                                final_i, final_j = i, j
                            if final_score>=beta:
                               return final_score, final_j
                            alpha=max(alpha,final_score)

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
                            final_i, final_j = i, j
                        if final_score1<=alpha:
                            return final_score1, final_j
                        beta=min(beta,final_score1)

        if first_time:
            board[final_i][final_j] = 'O'
        return final_score1,final_j


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




def main():
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
        board1.select_column(r)
        time.sleep(2)

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
