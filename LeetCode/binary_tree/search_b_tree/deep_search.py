#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#	  def __init__(self, x):
#		  self.val = x
#		  self.left = None
#		  self.right = None

"""
二叉树深度遍历
"""
### 递归版

# 前序遍历
class Solution:
	def __init__(self):
		"""
		结果输出列表初始化
		"""
		self.res = []
		
	def preorderTraversal(self, root: TreeNode) -> List[int]:
		
		def traversal(root):
			if not root:
				return
			self.res.append(root.val)
			self.preorderTraversal(root.left)
			self.preorderTraversal(root.right)
			
		# 执行递归代码
		traversal(root)
		return self.res

		
# 中序遍历
class Solution:
    def __init__(self):
        """
        结果输出列表初始化
        """
        self.res = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def traversal(root):
            if not root:
                return
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
            
        # 执行递归代码
        traversal(root)
        return self.res
		
		
# 后序遍历
class Solution:
    def __init__(self):
        """
        结果输出列表初始化
        """
        self.res = []
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        def traversal(root):
            if not root:
                return
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
            
        # 执行递归代码
        traversal(root)
        return self.res
		

### 迭代算法
# 前序遍历
class Solution:
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        思路：
            借助一个栈来实现
            通过先将其右孩子压入栈，再将其左孩子压入栈
        """
        if not root:
            return []
        # 辅助栈
        resStack = [root]
        # 结果列
        resList = []

        while resStack:
            node = resStack.pop()
            if node:
                resList.append(node.val)
                # 只有不为空时才操作
                if node.right:
                    resStack.append(node.right)
                if node.left:
                    resStack.append(node.left)
            
        return resList

# 中序遍历

class Solution:
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        思路：
            借助一个栈来实现
            优先找左孩子，再找右孩子
        """
        if not root:
            return []
        # 辅助栈
        resStack = []
        # 结果列
        resList = []
        
        node = root
        while resStack or node:
            while node:
			# 此处是为了记录对应的右结点的上级结点
                resStack.append(node)
                node = node.left
            node = resStack.pop()
            resList.append(node.val)
            node = node.right
            
        return resList
		
# 后序遍历
class Solution:
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        可以考虑先建立 根-右-左再反转
        """
        if not root:
            return []
        
        resStack = []
        resList = []
        
        node = root
        
        while resStack or node:
            
            while node:
                resList.append(node.val)
                resStack.append(node)
                node = node.right
            node = resStack.pop()
            node = node.left
        return resList[::-1]
		
def DFS(root):
	if root is None:
		return
	stack = []
	res = []
	stack.append(root)
	while stack:
		currentNode = stack.pop()
		res.append(currentNode.val)
		if currentNode.right:
			stack.append(currentNode.right)
		if currentNode.left:
			stack.append(currentNode.left)
	return res