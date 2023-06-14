#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        cur_layer = [root]
        last_node = None
        
        while len(cur_layer) > 0:
            next_layer = []
            for node in cur_layer:
                if last_node:
                    last_node.next = node
                last_node = node

                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            last_node = None
            node.next = last_node
            cur_layer = next_layer
        
        return root


# @lc code=end