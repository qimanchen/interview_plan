#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二叉树的最大深度
"""

# Definition for a binary tree node.
# class TreeNode:
#	  def __init__(self, x):
#		  self.val = x
#		  self.left = None
#		  self.right = None

# 自底而上
class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		
		if not root:
			return 0
			
		# 每次进入整个新的一层就加1
		return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
		

# 自顶而下
