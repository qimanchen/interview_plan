#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    BOARD_SIZE = 15

    # 定义一个二维列表来充当棋盘
    board = []

    def initBoard():
        # 位每个元素赋值"+"，用于控制台画出棋盘
        for i in range(BOARD_SIZE):
            row = ["+"] * BOARD_SIZE
            board.append(row)

    # 控制台输出棋盘的方法
    def printBoard():
        # 打印每个列表元素
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                # 打印列表元素后，不换行
                print(board[i][j], end="")
                # 没打印完一行，输出换行
            print()
    initBoard()
    printBoard()

    inputStr = input("请输入您的下棋的坐标，x,y的格式输出: \n")

    while inputStr != None:
        x_str, y_str = inputStr.split(sep=',')
        board[int(y_str) - 1] [int(x_str) - 1] = "."

        printBoard()
        inputStr = input("请输入您的下棋的坐标，x,y的格式输出: \n")

if __name__ == "__main__":
    main()
