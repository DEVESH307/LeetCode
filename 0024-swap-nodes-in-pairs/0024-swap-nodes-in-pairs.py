# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        cur = head

        while cur:
            node1 = cur
            cur = cur.next
            
            node2 = None
            if cur:
                node2 = cur
                cur = cur.next

            if node2:
                tail.next = node2
                tail = tail.next

                tail.next = node1
                tail = tail.next
            else:
                tail.next = node1
                tail = tail.next

        tail.next = None
        return dummy.next