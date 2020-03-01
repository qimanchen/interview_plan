#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数组中重复的数字
问题描述：
	找出数组中重复的数字。
	在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 
	的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
	也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例：
	输入：
	[2, 3, 1, 0, 2, 5, 3]
	输出：2 或 3 
"""
########方法一
class Solution(object):
	"""
	思路：
		利用题目中的条件，数组中值得范围为0~n-1
			如果当前数 nums[num] != index
				1. if nums[num] == num，则说明找到重复的数据
				2. if nums[num] != num，那么执行交换 nums[num],nums[index] =nums[index], nums[num]
	"""
    def findRepeatNumber(self, nums: List[int]) -> int:
        for index,value in enumerate(nums):
            if index != value:
                if nums[value] == value:
                    return value
                nums[index], nums[value] = nums[value], nums[index]
        return -1
########方法二
class Solution:
	"""
	思路：
		利用hash表的O(1)的索引特性
		利用hash表存储下每个数出现的次数
			1. 当num第一次出现时，将其增加到hash表中
			2. 当在hash表中直接访问到该数时，那么说明此数为重复数
	"""
    def findRepeatNumber(self, nums: List[int]) -> int:
        num_array = {}

        for num in nums:
            if num_array.get(num) == 1:
                return num
            num_array[num] = 1
        return -1
