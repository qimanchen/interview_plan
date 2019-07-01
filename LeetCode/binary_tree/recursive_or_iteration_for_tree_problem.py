#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二叉树问题的两种解法
"""

# 自顶而下
# 能够确定一些参数可以传递个子结点
"""
每个递归层级：
	首先访问结点来计算一些值，并在递归调用函数时将这些值传递到子结点
	先序遍历
	
	伪代码描述
	topDown(root, params):
		1. 对于空结点返回一个指定值;
		2. 如果需要更新结果，则更新;
		3. 左孩子传递
		left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
		4. 右孩子传递
		right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params
		5. return the answer if needed                      // answer <-- left_ans, right_ans
"""

# 自低向下
# 能够先解出子结点
"""
每个递归层次：
	首先对所有子结点递归调用函数，然后根据返回值和根结点本身的值得到答案
	后序遍历
	bottom_up(root):
		1. return specific value for null node
		2. left_ans = bottom_up(root.left)          // call function recursively for left child
		3. right_ans = bottom_up(root.right)        // call function recursively for right child
		4. return answers                           // answer <-- left_ans, right_ans, root.val
"""