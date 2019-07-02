#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
通过后序加中序还原二叉树
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if len(inorder)==0 and len(postorder)==0:
            return
        
        head = postorder[-1] # 对应的根结点
        headIndex = inorder.index(head) # 对应根结点的索引位置
        
        res = TreeNode(head)
		# 这里要特别注意一下postorder的取值范围
		# inorder去除根结点 -- 分割元素
		# postorder去除根结点 -- 最后一个元素
        res.left = self.buildTree(inorder[:headIndex], postorder[:headIndex])
        res.right = self.buildTree(inorder[headIndex+1:], postorder[headIndex:-1])
        return res