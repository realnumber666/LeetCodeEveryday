#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        left_to_right = True
        cur_layer = [root]

        while len(cur_layer) > 0:
            node_to_be_add = cur_layer if left_to_right else cur_layer[::-1]
            left_to_right = not left_to_right
            res.append([node.val for node in node_to_be_add])

            next_layer = []
            for node in cur_layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            cur_layer = next_layer
        return res


# @lc code=end

