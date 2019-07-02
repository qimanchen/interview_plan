#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
填充每一个结点的下一个右侧结点指针
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        层次遍历该版
        """
        if not root:
			# 注意排除这种特殊情况
            return None
        midRoot = root
        
		# 确定操作的第一层
        q = [midRoot]
        
        while q:
            nextQ = []
            while q:
				# 每一层检查其右边是否还有其他结点
                nowNode = q.pop(0)
                if q:
                    nowNode.next = q[0]
                else:
                    nowNode.next = None
				# 当存在左结点或右结点时加入下一层
                if nowNode.left:
                    nextQ.append(nowNode.left)
                if nowNode.right:
                    nextQ.append(nowNode.right)
            q = nextQ
        return root