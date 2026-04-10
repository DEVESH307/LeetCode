"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# from collections import deque
# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if not root:
#             return root
        
#         q = deque([root])

#         while q:
#             size = len(q)
#             prev = None

#             for _ in range(size):
#                 node = q.popleft()

#                 if prev:
#                     prev.next = node
#                 prev = node

#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)

#             prev.next = None

#         return root
        

class Solution:
    def getNextChild(self, node):
        temp = node.next

        while temp:
            if temp.left:
                return temp.left
            if temp.right:
                return temp.right
            temp = temp.next
        
        return None


    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        level = root

        while level:
            curr = level
            while curr:
                if curr.left:
                    if curr.right:
                        curr.left.next = curr.right
                    else:
                        curr.left.next = self.getNextChild(curr)

                if curr.right:
                    curr.right.next = self.getNextChild(curr)

                curr = curr.next
            
            if level.left:
                level = level.left
            elif level.right:
                level = level.right
            else:
                level = self.getNextChild(level)

        return root
