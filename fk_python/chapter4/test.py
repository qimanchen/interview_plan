#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_t(n):
    if n%2 == 0:
        print("不可打印")
        return
    mid = n //2 + 1

    # 打印上层
    sor = list(range(mid))
    sor2 = sor[:-1]

    for i, j in zip(sor[::-1], sor):
        if j== 0:
            print(" "*i +"*" + " " *(2*j+1-2))
            continue
        print(" "*i +"*" + " " *(2*j+1-2) + "*")
        # print(" "*i + (2*j +1)*"*")

    for i,j in zip(sor2, sor2[::-1]):
        if j== 0:
            print(" "*(i+1) +"*" + " " *(2*j+1-2))
            continue
        print(" "*(i +1)+"*" + " " *(2*j+1-2) + "*")
        # print(" "*(i +1)+ (2*j +1)*"*")


if __name__ == "__main__":
    print_t(7)
