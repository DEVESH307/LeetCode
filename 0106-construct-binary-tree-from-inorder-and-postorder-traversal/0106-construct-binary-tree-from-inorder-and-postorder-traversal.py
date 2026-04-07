# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.setrecursionlimit(10**6)
class Solution:
    def buildTreeHelper(self, Post, In, sPost, ePost, sIn, eIn, index_map):
        if sPost > ePost or sIn > eIn:
            return None

        root_val = Post[ePost]
        root = TreeNode(root_val)

        idx = index_map[root_val]
        left_size = idx - sIn

        root.left = self.buildTreeHelper(
            Post, In,
            sPost, sPost + left_size - 1,
            sIn, idx - 1,
            index_map
        )

        root.right = self.buildTreeHelper(
            Post, In,
            sPost + left_size, ePost - 1,
            idx + 1, eIn,
            index_map
        )

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        In = inorder
        Post = postorder

        index_map = {val: i for i, val in enumerate(In)}
        return self.buildTreeHelper(Post, In, 0, len(Post)-1, 0, len(In)-1, index_map)        