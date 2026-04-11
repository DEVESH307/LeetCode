# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def search(self, node, target):
        if not node:
            return False
        
        if node == target:
            self.path.append(node)
            return True

        if self.search(node.left, target) or self.search(node.right, target):
            self.path.append(node)
            return True

        return False


    def below(self, node, k):
        if not node or k < 0:
            return

        if k == 0:
            self.result.append(node.val)
            return

        self.below(node.left, k - 1)
        self.below(node.right, k - 1)


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.search(root, target)

        # nodes below target
        self.below(self.path[0], k)

        # ancestors
        for i in range(1, len(self.path)):
            dist = k - i

            if dist == 0:
                self.result.append(self.path[i].val)
                continue

            parent = self.path[i]
            child = self.path[i - 1]

            if parent.left == child:
                self.below(parent.right, dist - 1)
            else:
                self.below(parent.left, dist - 1)

        return self.result