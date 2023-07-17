#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        cur_layer = [root]
        next_layer = []

        while len(cur_layer) > 0:
            for n in cur_layer:
                if n.left:
                    next_layer.append(n.left)
                if n.right:
                    next_layer.append(n.right)
        
            res.append([n.val for n in cur_layer])
            cur_layer = next_layer
            next_layer = []
        
        return res  

# @lc code=end

