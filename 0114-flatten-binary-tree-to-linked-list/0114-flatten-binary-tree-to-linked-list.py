# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None, None

        l_head, l_tail = self.flatten(root.left)
        r_head, r_tail = self.flatten(root.right)
        root.left = None

        if not l_head and not r_head:
            return root, root
        elif not l_head:
            root.right = r_head
            return root, r_tail
        elif not r_head:
            root.right = l_head
            return root, l_tail
        else:
            root.right = l_head
            l_tail.right = r_head
            return root, r_tail