'''将空白Cell左边的Cell右移到空白Cell位置'''
# board数组的值记录原来块打乱后的位置
import random

from renwu.pingtugame import cfg


def moveR(board, index, columns):
    if index % columns == 0: return index
    board[index - 1], board[index] = board[index], board[index - 1]
    return index - 1


'''将空白Cell右边的Cell左移到空白Cell位置'''


def moveL(board, index, columns):
    if (index + 1) % columns == 0: return index
    board[index + 1], board[index] = board[index], board[index + 1]
    return index + 1


'''将空白Cell上边的Cell下移到空白Cell位置'''


def moveD(board, index, columns):#向下标减小的方向移动
    if index < columns: return index
    board[index - columns], board[index] = board[index], board[index - columns]
    return index - columns


'''将空白Cell下边的Cell上移到空白Cell位置'''


def moveU(board, index, rows, columns):#向下标增大的方向移动
    if index >= (rows - 1) * columns: return index
    board[index + columns], board[index] = board[index], board[index + columns]
    return index + columns


'''获得打乱的拼图'''


def CreateBoard(rows, columns, sum_chunk):#移动的是空白块
    board = []  # 整个的核心
    #初始化board
    for i in range(sum_chunk):
        board.append(i)
    # 去掉右下角那块
    index = sum_chunk - 1
    board[index] = -1
    for i in range(cfg.NUMRANDOM):
        # 0: left, 1: right, 2: up, 3: down
        direction = random.randint(0, 3)
        if direction == 0:
            index = moveL(board, index, columns)
        elif direction == 1:
            index = moveR(board, index, columns)
        elif direction == 2:
            index = moveU(board, index, rows, columns)
        elif direction == 3:
            index = moveD(board, index, columns)
    return board, index
