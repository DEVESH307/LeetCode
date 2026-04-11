# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        q = deque([root])
        result = []
        
        while q:
            node = q.popleft()

            if not node:
                result.append("null")
            else:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ",".join(result) 


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] is None:
            return None

        data = data.split(",")
        root = TreeNode(int(data[0]))
        q = deque([root])
        i = 1

        while q and i < len(data):
            node = q.popleft()

            if data[i] != "null":
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            if data[i+1] != "null":
                node.right = TreeNode(int(data[i+1]))
                q.append(node.right)

            i += 2

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))