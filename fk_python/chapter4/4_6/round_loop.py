#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def loop_test(n):
    """
    输出
    """
    # 初始化
    result = [[0 for i in range(n)] for j in range(n)]

    # 循环转圈
    # orient代表转圈的方向
    # 0 向下，1代表向右，2代表向左，3代表向上
    orient = 0

    # j控制行索引，k控制列索引
    j = 0
    k = 0

    for i in range(1, n*n +1):
        result[j][k] = i

        if j + k == n -1:
            if j > k:
                orient = 1
            else:
                orient = 2
        elif (k==j) and (k >= n/2):
            orient = 3
        elif (j == k-1) and (k <= n/2):
            orient = 0
        # 控制移动
        if orient == 0:
            j += 1
        elif orient == 1:
            k += 1
        elif orient == 2:
            k -= 1
        elif orient == 3:
            j -= 1
    for i in range(n):
        for j in range(n):
            print('%02d' % result[i][j], end=" ")
        print("")


if __name__ == "__main__":
    loop_test(4)

