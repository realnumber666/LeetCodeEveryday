# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = [root]

        if stack is not None:
            node = stack.pop()
            stack.append(node.right)
            stack.append(node.left)

