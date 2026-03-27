"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         if not head:
#             return None

#         node_map = {}

#         # Step 1: create all nodes
#         curr = head
#         while curr:
#             node_map[curr] = Node(curr.val)
#             curr = curr.next

#         # Step 2: assign next and random
#         curr = head
#         while curr:
#             copy = node_map[curr]
#             copy.next = node_map.get(curr.next)
#             copy.random = node_map.get(curr.random)
#             curr = curr.next

#         return node_map[head]


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # interleave lists
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # seprqate lists
        # curr = head
        # head2 = curr.next
        # curr2 = head2

        # while curr:
        #     curr.next = curr2.next
        #     if curr2.next:
        #         curr = curr.next
        #         curr2.next = curr.next
        #         curr2 = curr2.next
        #     else:
        #         break

        curr = head
        dummy = Node(0)
        copy_curr = dummy
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy_curr.next = copy
            copy_curr = copy
            curr = curr.next

        return dummy.next

            