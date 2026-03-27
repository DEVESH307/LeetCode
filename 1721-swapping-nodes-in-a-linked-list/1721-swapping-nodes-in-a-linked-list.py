# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if not head:
#             return head

#         slow = fast = head
#         prev1 = prev2 = None

#         # find kth from start
#         for _ in range(k - 1):
#             prev1 = fast
#             fast = fast.next
#         head1 = fast

#         # find kth from end
#         while fast.next:
#             prev2 = slow
#             slow = slow.next
#             fast = fast.next
#         head2 = slow

#         # same node → no swap
#         if head1 == head2:
#             return head

#         # fix prev pointers
#         if prev1:
#             prev1.next = head2
#         else:
#             head = head2

#         if prev2:
#             prev2.next = head1
#         else:
#             head = head1

#         # swap next pointers (only one temp)
#         temp = head1.next
#         head1.next = head2.next
#         head2.next = temp

#         return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        slow = fast = head

        for _ in range(k - 1):
            fast = fast.next
        head1 = fast

        while fast.next:
            slow = slow.next
            fast = fast.next
        head2 = slow

        if head1 == head2:
            return head

        head1.val, head2.val = head2.val, head1.val
        return head