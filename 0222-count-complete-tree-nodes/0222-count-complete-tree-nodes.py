# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         def dfs(root):
#             if not root:
#                 return 0

#             if not root.left and not root.right:
#                 return 1

#             return 1 + dfs(root.left) + dfs(root.right)

#         return dfs(root)


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_height(node):
            ht = 0
            while node:
                node = node.left
                ht += 1
            return ht

        def right_height(node):
            ht = 0
            while node:
                node = node.right
                ht += 1
            return ht

        if not root:
            return 0

        lh = left_height(root)
        rh = right_height(root)

        if lh == rh:
            return (1 << lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)