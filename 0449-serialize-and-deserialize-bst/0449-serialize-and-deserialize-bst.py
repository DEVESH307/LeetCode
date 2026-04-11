# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        result = []

        def preorder(node):
            if not node:
                return

            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(result)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        data = list(map(int, data.split(",")))
        self.i = 0

        def build(low, high):
            if self.i == len(data):
                return None

            val = data[self.i]
            if not (low < val < high):
                return None

            self.i += 1
            root = TreeNode(val)

            root.left = build(low, val)
            root.right = build(val, high)
            return root

        return build(float('-inf'), float('inf'))        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans