# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def dfs(node):
#             if not node:
#                 return

#             dfs(node.left)
#             dfs(node.right)
#             result.append(node.val)

#         dfs(root)
#         return result


# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []

#         stack = [root]
#         result = []

#         while stack:
#             node = stack.pop()
#             result.append(node.val)

#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)

#         return result[::-1]


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def addPath(node):
            start = node
            path = []
            while node:
                path.append(node.val)
                node = node.right
            result.extend(path[::-1])

        dummy = TreeNode(0)
        dummy.left = root

        result = []
        curr = dummy

        while curr:
            if curr.left:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    addPath(curr.left)
                    curr = curr.right
            else:
                curr = curr.right

        return result