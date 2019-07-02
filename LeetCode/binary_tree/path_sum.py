#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
路径总和
给定一个二叉树和一个目标和，
判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		if not root:
            return False
        
        sum -= root.val # 每次递减相应的数值
        
        if not root.right and not root.left:
			# 判断到达叶子结点
            return sum == 0
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
		
	
# 迭代
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        
        q = [(root, sum)]
        
        while q:
            nextQ = []
            # 每次更新对应层的队列
            for i in q:
                if (i[1] - i[0].val) == 0 and not i[0].right and not i[0].left:
					# 找到叶子结点，并对应的sum值为0
                    return True
                if i[0].left:
                    nextQ.append((i[0].left, i[1] - i[0].val))
                if i[0].right:
                    nextQ.append((i[0].right, i[1] - i[0].val))
            
            q = nextQ
        return False