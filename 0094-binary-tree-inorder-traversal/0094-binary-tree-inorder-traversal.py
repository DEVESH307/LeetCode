# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def dfs(node):
#             if not node:
#                 return
            
#             dfs(node.left)
#             result.append(node.val)
#             dfs(node.right)

#         dfs(root)

#         return result


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        result = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result