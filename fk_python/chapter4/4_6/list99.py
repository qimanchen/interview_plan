#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print99():
    """
    打印99乘法表
    """

    i = 1
    j = 1
    while i < 10:

        if i == j:
            print("%d x %d = %d" % (j, i, i*j))
            j = 1
            i += 1
        else:
            print("%d x %d = %d" % (j, i, i*j), end=", ")
            j += 1


if __name__ == "__main__":
    print99()

