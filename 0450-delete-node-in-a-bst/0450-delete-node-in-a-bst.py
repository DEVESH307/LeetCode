# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMaxOfLST(self, root):
        while root.right:
            root = root.right
        return root
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1: no child
            if not root.left and not root.right:
                return None
            
            # case 2: one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # case 3: two children
            pred = self.getMaxOfLST(root.left)
            root.val = pred.val
            root.left = self.deleteNode(root.left, pred.val)

        return root