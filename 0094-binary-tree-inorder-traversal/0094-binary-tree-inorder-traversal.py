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


# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []

#         stack = []
#         result = []
#         node = root

#         while node or stack:
#             while node:
#                 stack.append(node)
#                 node = node.left

#             node = stack.pop()
#             result.append(node.val)
#             node = node.right

#         return result


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    result.append(curr.val)
                    curr = curr.right

        return result