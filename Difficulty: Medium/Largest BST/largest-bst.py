class NodeInfo:
    def __init__(self, isBST, max_size, own_size, max_val, min_val):
        self.isBST = isBST
        self.max_size = max_size
        self.own_size = own_size
        self.max_val = max_val
        self.min_val = min_val


class Solution:
    def largestBst(self, root):

        def dfs(node):
            if not node:
                return NodeInfo(True, 0, 0, float('-inf'), float('inf'))

            left = dfs(node.left)
            right = dfs(node.right)

            isBST = (
                left.isBST and
                right.isBST and
                left.max_val < node.data < right.min_val
            )

            if isBST:
                own_size = left.own_size + right.own_size + 1
                max_val = max(node.data, right.max_val)
                min_val = min(node.data, left.min_val)
            else:
                own_size = 0
                max_val = float('inf')
                min_val = float('-inf')

            max_size = max(left.max_size, right.max_size, own_size)

            return NodeInfo(isBST, max_size, own_size, max_val, min_val)

        return dfs(root).max_size