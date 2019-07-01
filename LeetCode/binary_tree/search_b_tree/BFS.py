#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#	  def __init__(self, x):
#		  self.val = x
#		  self.left = None
#		  self.right = None


# 递归版

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
		
		resList = []
		
		def helper(root, depth):
			"""
			每一层一层递归
			"""
			if len(resList) == depth:
				# 每次检测到进入新的一层
				resList.append([])
				
			resList[depth].append(root.val)
			helper(root.left, depth+1)
			helper(root.right, depth+1)
			
		helper(root, 0)
		return resList
		
		
# 迭代版
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
		"""
		通过分成两个队列
		1. 当前层队列
		2. 下一层队列
		每一次从根据当前队列找出下一层的结点
		操作完一层后，更新当前层（为下一层）
		重复，直到队列为空
		"""
		
		resQueue = [root]
		resList = []
		
		while resQueue:
			# 记录下一层结点
			nextQueue = []
			item = []
			for node in resQueue:
				# 判断是否为None
				if node:
					item.append(node.val)
					# 可能会加入为None的结点
					nextQueue.append(node.left)
					nextQueue.append(node.right)
			if item:
				# 每次插入新的一层的数据
				resList.append(item)
			# 更新当前层队列
			queue = nextQueue
		return resList