# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         arr = []

#         def inorder(node):
#             if not node:
#                 return
#             inorder(node.left)
#             arr.append(node.val)
#             inorder(node.right)

#         inorder(root)

#         i, j = 0, len(arr) - 1
#         while i < j:
#             s = arr[i] + arr[j]
#             if s == k:
#                 return True
#             elif s < k:
#                 i += 1
#             else:
#                 j -= 1

#         return False


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False

            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return True if dfs(root) else False