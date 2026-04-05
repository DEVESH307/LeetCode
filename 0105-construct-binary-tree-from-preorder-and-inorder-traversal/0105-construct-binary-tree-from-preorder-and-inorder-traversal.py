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
        if sPre > ePre:
            return None

        root = TreeNode(Pre[sPre])
        idx = index_map.get(Pre[sPre])
        x = idx - sIn
        root.left = self.buildTreeHelper(Pre, In, sPre+1, sPre+x, sIn, idx-1, index_map)
        root.right = self.buildTreeHelper(Pre, In, sPre+x+1, ePre, idx+1, eIn, index_map)

        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val: i for i, val in enumerate(inorder)}
        root = self.buildTreeHelper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1, index_map)
        
        return root        