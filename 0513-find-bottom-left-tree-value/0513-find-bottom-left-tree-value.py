# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque
# class Solution:
#     def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return []

#         q = deque([root])

#         while q:
#             node = q.popleft()
#             if node.right:
#                 q.append(node.right)
#             if node.left:
#                 q.append(node.left)

#         return node.val


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = -1
        self.ans = None

        def dfs(node, depth):
            if not node:
                return

            if depth > self.max_depth:
                self.max_depth = depth
                self.ans = node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return self.ans