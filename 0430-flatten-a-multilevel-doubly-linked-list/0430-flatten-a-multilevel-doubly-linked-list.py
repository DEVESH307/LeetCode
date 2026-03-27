"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head
        while curr:
            if curr.child:
                # flatten the child Node
                last = curr.next
                curr.next = self.flatten(curr.child)
                
                curr.next.prev = curr
                curr.child = None

                # find tail of new linked list
                while curr.next:
                    curr = curr.next

                # attach the tail with next ptr
                if last:
                    curr.next = last
                    last.prev = curr
            curr = curr.next
            
        return head