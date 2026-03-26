# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur:
            # move cur to the end of duplicates (if any)
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            if prev.next == cur:
                prev = prev.next
            else:
                prev.next = cur.next

            cur = cur.next

        return dummy.next
            