# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxProduct(self, root: Optional[TreeNode]) -> int:
#         MOD = 10**9+7
#         self.max_prod = 0

#         def tree_sum(root):
#             if not root:
#                 return 0
#             return root.val + tree_sum(root.left) + tree_sum(root.right)

#         total = tree_sum(root)

#         def dfs(root):
#             if not root:
#                 return 0

#             left_sum = dfs(root.left)
#             right_sum = dfs(root.right)
            
#             curr_sum = root.val + left_sum + right_sum
#             curr_prod = curr_sum * (total - curr_sum)
#             self.max_prod = max(self.max_prod, curr_prod)

#             return curr_sum

#         dfs(root)

#         return self.max_prod % MOD


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9+7
        sums = []

        def tree_sum(root):
            if not root:
                return 0
            s = root.val + tree_sum(root.left) + tree_sum(root.right)
            sums.append(s)
            return s

        total = tree_sum(root)
        return max(s * (total-s) for s in sums) % MOD