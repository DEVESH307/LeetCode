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

    # reverse list
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

    # compare two list
    def compareList(self, head1, head2):
        while head2 and head1.val == head2.val:
            head1 = head1.next
            head2 = head2.next

        return head2 is None


    # palindrome
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        head1 = head
        mid = self.getFirstMid(head1)
        head2 = mid.next
        mid.next = None

        # reverse 2nd half
        head2 = self.reverseList(head2)

        return self.compareList(head1, head2)
        