# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def dfs(node):
#             if not node:
#                 return

#             result.append(node.val)
#             dfs(node.left)
#             dfs(node.right)

#         dfs(root)
#         return result


# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []

#         stack = [root]
#         result = []

#         while stack:
#             node = stack.pop()
#             result.append(node.val)

#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)

#         return result


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root

        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    result.append(curr.val)
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    curr = curr.right

        return result