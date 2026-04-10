# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeHeight(self, root):
        if not root:
            return -1

        left_height = self.treeHeight(root.left)
        right_height = self.treeHeight(root.right)

        return 1 + max(left_height, right_height)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        left_dia = self.diameterOfBinaryTree(root.left)
        right_dia = self.diameterOfBinaryTree(root.right)

        height_LST = self.treeHeight(root.left)
        height_RST = self.treeHeight(root.right)

        return max(left_dia, right_dia, height_LST + height_RST + 2)