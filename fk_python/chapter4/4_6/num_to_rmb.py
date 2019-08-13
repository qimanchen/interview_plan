#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
数字转人名币读法

说明：
    把一个浮点数分解成整数部分和小数部分字符串
    num 是需要被分解的浮点数
    返回分解出来的整数部分和小数部分
    第一个数组元素时整数部分，第二个数组是小数部分
"""

def divide(num):
    # 将num换成字符串（整数部分和小数部分）
    integer, fraction = num.split('.')
    return integer, fraction

def four_to_hanstr(num_str, han_list, unit_list):
    """
    把一个4位的数字字符串变成汉字字符串
    num_str 是需要转换的数字字符串
    返回4位数字字符串被转换成汉字字符串
    """

    result = ""

    num_len = len(num_str)
    flag = None
    flag1 = None
    for i in range(num_len):
        if flag is None:
            flag = num_str[i]
        flag1 = num_str[i]
        if flag1 != flag:
            flag = flag1
            num = int(num_str[i])
        elif flag1 == flag and flag =="0":
            num = '-'
            flag = flag1
        else:
            num = int(num_str[i])

        if i != num_len - 1 and num != 0 and num != '-':
            result += han_list[num] + unit_list[num_len-2-i]
        else:
            if num == '-':
                pass
            else:
                result += han_list[num]
    return result

def integer_to_str(num_str):
    # 处理整个转换过程
    han_list = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
    unit_list = ["十", "百", "千"]

    str_len = len(num_str)

    if str_len > 12:
        print('数字太大，翻译不了')
        return
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8],han_list, unit_list) + "亿" +\
                four_to_hanstr(num_str[-8:-4], han_list, unit_list) + "万" +\
                four_to_hanstr(num_str[-4:], han_list, unit_list)
    elif str_len > 4:
        return four_to_hanstr(num_str[:-4], han_list, unit_list) + "万" +\
                four_to_hanstr(num_str[-4:], han_list, unit_list)
    else:
        return four_to_hanstr(num_str, han_list, unit_list)

def fraction_to_str(fraction):
    """
    将小数部分进行分离
    """
    fraction_part = ['角', '分', '厘', '毫']
    han_list = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]

    result = ""
    if len(fraction) > 4:
        fraction = fraction[:4]
    for i in range(len(fraction)):
        if int(fraction[i]) == 0:
            pass
        else:
            result += han_list[int(fraction[i])] + fraction_part[i]
    return result

def main():
    # 测试

    num = input("请输入一个浮点数: ")

    integer, fraction = divide(num)

    print(integer_to_str(integer))
    print(fraction_to_str(fraction))


if __name__ == "__main__":
    main()
    
