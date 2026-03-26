# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next
            
        cur = prev.next

        head2 = None
        next_node = cur

        for _ in range(right-left+1):
            temp = next_node
            next_node = next_node.next
            temp.next = head2
            head2 = temp

        prev.next = head2
        cur.next = next_node

        return dummy.next
        