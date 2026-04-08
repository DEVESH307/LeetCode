# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def height(self, root):
#         if not root:
#             return 0

#         left_height = self.height(root.left)
#         right_height = self.height(root.right)

#         return 1 + max(left_height, right_height)

        
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True

#         left_height = self.height(root.left)
#         right_height = self.height(root.right)

#         if abs(left_height - right_height) > 1:
#             return False

#         return self.isBalanced(root.left) and self.isBalanced(root.right)
        

# # Binary tree node info
# class NodeInfo:
#     def __init__(self, balanced, height):
#         self.balanced = balanced
#         self.height = height 

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         def dfs(node):
#             if not node:
#                 return NodeInfo(True, -1)

#             left = dfs(node.left)
#             right = dfs(node.right)

#             balanced = (
#                 left.balanced and
#                 right.balanced and
#                 abs(left.height - right.height) <= 1
#             )
            
#             height = max(left.height, right.height) + 1

#             return NodeInfo(balanced, height)

#         return dfs(root).balanced


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return True if dfs(root) != -1 else False