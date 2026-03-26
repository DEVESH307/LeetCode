# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getFirstMid(self, head):
        if not head or not head.next:
            return head

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # merge 2 sorted list
    def mergeTwoLists(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
            
        tail = None
        if head1.val < head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next

        tail = head

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                # tail = tail.next
                head1 = head1.next
            else:
                tail.next = head2
                # tail = tail.next
                head2 = head2.next
            
            tail = tail.next

        tail.next = head1 if head1 else head2

        return head

    # sort list
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.getFirstMid(head)
        head2 = mid.next
        mid.next = None

        head1 = self.sortList(head)
        head2 = self.sortList(head2)

        return self.mergeTwoLists(head1, head2)