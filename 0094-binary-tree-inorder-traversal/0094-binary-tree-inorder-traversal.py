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
        stack = []
        result = []

        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack.pop()
                result.append(temp.val)
                curr = temp.right

        return result