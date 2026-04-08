# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         sorted_arr = []

#         def inorder(node):
#             if not node:
#                 return

#             inorder(node.left)
#             sorted_arr.append(node.val)
#             inorder(node.right)

#         inorder(root)
#         return sorted_arr[k-1]



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return

            left = inorder(node.left)
            if left is not None:
                return left

            nonlocal k
            k -= 1
            if k == 0:
                return node.val

            return inorder(node.right)

        return inorder(root)
        