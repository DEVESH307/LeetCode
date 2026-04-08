# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         self.prev = float('-inf')

#         def inorder(node):
#             if not node:
#                 return True

#             if not inorder(node.left):
#                 return False

#             if node.val <= self.prev:
#                 return False
#             self.prev = node.val

#             return inorder(node.right)
        
#         return inorder(root)



# class NodeInfo:
#     def __init__(self, min_val, max_val, isBST):
#         self.min_val = min_val
#         self.max_val = max_val
#         self.isBST = isBST

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def dfs(node):
#             if not node:
#                 return NodeInfo(float('inf'), float('-inf'), True)

#             left = dfs(node.left)
#             right = dfs(node.right)

#             isBST = left.isBST and right.isBST and left.max_val < node.val < right.min_val
#             min_val = min(left.min_val, node.val)
#             max_val = max(right.max_val, node.val)
#             return NodeInfo(min_val, max_val, isBST)

#         return dfs(root).isBST


# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def dfs(node):
#             if not node:
#                 return True, float('inf'), float('-inf')

#             l_bst, l_min, l_max = dfs(node.left)
#             r_bst, r_min, r_max = dfs(node.right)

#             isBST = l_bst and r_bst and l_max < node.val < r_min
#             min_val = min(l_min, node.val)
#             max_val = max(r_max, node.val)

#             return isBST, min_val, max_val

#         return dfs(root)[0]


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return (
                dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high)
            )

        return dfs(root, float('-inf'), float('inf'))