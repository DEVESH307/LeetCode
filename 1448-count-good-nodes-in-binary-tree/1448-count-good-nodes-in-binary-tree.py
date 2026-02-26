# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_so_far):
            if not root:
                return 0

            count = 0

            if root.val >= max_so_far:
                count = 1
                max_so_far = root.val

            left_count = dfs(root.left, max_so_far)
            right_count = dfs(root.right, max_so_far)

            return count + left_count + right_count

        return dfs(root, max_so_far = float('-inf'))
        