# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def swap(self, head1, head2):
#         head1.next = head2.next
#         head2.next = head1
#         return head2

#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head
#         prev = dummy
#         cur = head

#         while cur and cur.next:
#             new_head = self.swap(cur, cur.next)
#             prev.next = new_head
#             prev = cur
#             cur = cur.next

#         return dummy.next


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