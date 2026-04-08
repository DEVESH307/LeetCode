# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr, l, r):
            if l > r:
                return None
                
            mid = l + (r - l) // 2
            root = TreeNode(arr[mid])

            root.left = dfs(arr, l, mid-1)
            root.right = dfs(arr, mid+1, r)

            return root

        return dfs(nums, 0, len(nums)-1)        