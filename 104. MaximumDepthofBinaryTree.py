# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #         '''
        #         层序遍历
        #         '''
        #         if root is None:
        #             return 0

        #         cur_node = [root]
        #         next_node = []
        #         ret = 0

        #         while cur_node or next_node:
        #             for node in cur_node:
        #                 if node.left:
        #                     next_node.append(node.left)
        #                 if node.right:
        #                     next_node.append(node.right)

        #             ret += 1
        #             cur_node = next_node
        #             next_node = []

        #         return ret

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0