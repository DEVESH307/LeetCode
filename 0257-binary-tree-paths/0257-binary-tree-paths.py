# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         result = []
#         def dfs(root, path):
#             if not root:
#                 return

#             if path:
#                 path = path + "->" + str(root.val)
#             else:
#                 path = str(root.val)
            
#             if not root.left and not root.right:
#                 result.append(path)
#                 return

#             dfs(root.left, path)
#             dfs(root.right, path)

#         dfs(root, "")
#         return result


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(root, path):
            if not root:
                return

            path.append(str(root.val))
            
            if not root.left and not root.right:
                result.append("->".join(path))

            dfs(root.left, path)
            dfs(root.right, path)

            path.pop()

        dfs(root, [])
        return result
