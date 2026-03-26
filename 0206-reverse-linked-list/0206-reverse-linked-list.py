# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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