# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = True

    def isBalanced(self, root: TreeNode) -> bool:
        '''
        从root开始，一层一层拿到每一个子树的最大深度
        如果左右子树深度差大于1则false
        '''
        self.maxDepth(root)
        return self.result

    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            if abs(l - r) > 1:
                self.result = False
            return max(l, r) + 1