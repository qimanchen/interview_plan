#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
面向切片编程-AOP
装饰器
"""

def auth(fn):
    """
    装饰器外层
    """
    def auth_fn(*args, **kwargs):
        """
        装饰操作参数
        """
        # 用一条语句模拟执行权限检查
        print("----模拟执行检查中----")
        # 回调被装饰的目标函数
        fn_return = fn(*args)
        return fn_return
    return auth_fn

# 实现装饰
@auth
def test(a, b):
    """
    """
    print("执行test函数，参数a:%s, 参数b:%s" % (a, b))


if __name__ == "__main__":
    # 执行test
    test(20, 15)

