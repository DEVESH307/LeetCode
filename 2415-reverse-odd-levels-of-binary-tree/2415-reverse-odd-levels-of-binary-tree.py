# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []

        result = []
        q = deque([root])
        level = 0

        while q:
            curr_level = []

            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level % 2 == 1:
                i, j = 0, len(curr_level) - 1
                while i < j:
                    curr_level[i].val, curr_level[j].val = curr_level[j].val, curr_level[i].val
                    i += 1
                    j -= 1

            level += 1

        return root