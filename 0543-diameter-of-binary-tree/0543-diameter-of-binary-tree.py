# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def treeHeight(self, root):
#         if not root:
#             return -1

#         left_height = self.treeHeight(root.left)
#         right_height = self.treeHeight(root.right)

#         return 1 + max(left_height, right_height)


#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return -1
        
#         left_dia = self.diameterOfBinaryTree(root.left)
#         right_dia = self.diameterOfBinaryTree(root.right)

#         height_LST = self.treeHeight(root.left)
#         height_RST = self.treeHeight(root.right)

#         return max(left_dia, right_dia, height_LST + height_RST + 2)


class NodeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameterOfBinaryTreeHelper(root).diameter

    def diameterOfBinaryTreeHelper(self, root):
        if not root:
            return NodeInfo(-1, 0)

        left = self.diameterOfBinaryTreeHelper(root.left)
        right = self.diameterOfBinaryTreeHelper(root.right)

        height = max(left.height, right.height) + 1
        diameter = max(
            left.diameter,
            right.diameter,
            left.height + right.height + 2
        )

        return NodeInfo(height, diameter)