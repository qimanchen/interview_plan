#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
通过前序加中序还原二叉树
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return
        head = preorder[0] # 根结点的值
        headIndex = inorder.index(head) # 对应的根结点的位置在两个排序列表中
		# 构建treeNode
        res = TreeNode(head)
		# 注意这里面的索引的范围
        res.left = self.buildTree(preorder[1:headIndex+1], inorder[:headIndex])
        res.right = self.buildTree(preorder[headIndex+1:], inorder[headIndex+1:])
        return res