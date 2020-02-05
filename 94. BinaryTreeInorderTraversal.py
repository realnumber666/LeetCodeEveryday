# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []
        ret = []
        stack = []
        cur = root

        while cur is not None or stack is not None:
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            if stack == []:
                break
            node = stack.pop()
            # if node:
            ret.append(node.val)
            cur = node.right

        return ret