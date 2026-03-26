# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
            
        head2 = None
        next_node = head

        while next_node:
            temp = next_node
            next_node = next_node.next
            temp.next = head2
            head2 =temp
        
        return head2
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split list
        head2 = slow.next
        slow.next = None
        # reverse second half
        head2 = self.reverseList(head2)
        head1 = head

        # merge safely
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head2.next = next1

            head1 = next1
            head2 = next2

        return head
            
