# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.setrecursionlimit(10**6)
class Solution:
    def buildTreeHelper(self, Pre, In, sPre, ePre, sIn, eIn, index_map):
        if sPre > ePre or sIn > eIn:
            return None

        root_val = Pre[sPre]
        root = TreeNode(root_val)

        idx = index_map[root_val]
        left_size = idx - sIn

        root.left = self.buildTreeHelper(
            Pre, In,
            sPre + 1, sPre + left_size,
            sIn, idx - 1,
            index_map
        )

        root.right = self.buildTreeHelper(
            Pre, In,
            sPre + left_size + 1, ePre,
            idx + 1, eIn,
            index_map
        )

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val: i for i, val in enumerate(inorder)}
        return self.buildTreeHelper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1, index_map)    