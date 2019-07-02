#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
对称二叉树
"""
# 递归
# Definition for a binary tree node.
# class TreeNode:
#	  def __init__(self, x):
#		  self.val = x
#		  self.left = None
#		  self.right = None

class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		
		return self.helper(root, root)
	
	def helper(self, t1, t2):
		"""
		重点选出两个比较的点
		左对右
		右对左
		"""
		if t1 is None and t2 is None:
			return True
		if t1 is None or t2 is None:
			return False
		return t1.val==t2.val and self.helper(t1.right, t2.left) and self.helper(t1.left, t2.right)

# 迭代
class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		
		q = []
		
		q.append(root)
		q.append(root)
		
		while q:
			t1 = q.pop(0)
			t2 = q.pop(0)
			
			if t1 is None and t2 is None:
				continue
			# 注意这两个的判断不能变
			if t1 is None or t2 is None:
				return False
			if t1.val != t2.val:
				return False
			# 成对入队列
			q.append(t1.left)
			q.append(t2.right)
			q.append(t1.right)
			q.append(t2.left)
		return True
