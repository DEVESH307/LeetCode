# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque
# class Solution:
#     def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
#         q = deque([root])
#         level = 0

#         while q:
#             prev = None

#             for _ in range(len(q)):
#                 node = q.popleft()

#                 # value parity check
#                 if level % 2 == node.val % 2:
#                     return False

#                 # ordering check
#                 if prev is not None:
#                     if level % 2 == 0 and node.val <= prev:
#                         return False
#                     if level % 2 == 1 and node.val >= prev:
#                         return False
#                 prev = node.val

#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)

#             level += 1

#         return True


from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        even_level = True

        while q:
            prev = float('-inf') if even_level else float('inf')

            for _ in range(len(q)):
                node = q.popleft()

                if even_level:
                    if node.val % 2 == 0 or node.val <= prev:
                        return False
                else:
                    if node.val % 2 == 1 or node.val >= prev:
                        return False
                
                prev = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            even_level = not even_level

        return True