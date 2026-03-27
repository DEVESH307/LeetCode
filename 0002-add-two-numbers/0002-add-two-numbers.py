# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        head1 = l1
        head2 = l2
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while head1 or head2 or carry:
            total = 0

            if head1:
                total += head1.val
                head1 = head1.next

            if head2:
                total += head2.val
                head2 = head2.next

            if carry:
                total += carry

            tail.next = ListNode(total%10)
            tail = tail.next
            
            carry = total // 10

        return dummy.next
        