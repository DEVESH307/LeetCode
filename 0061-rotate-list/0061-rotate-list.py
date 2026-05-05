# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Normalize k
        k %= length
        if k == 0:
            return head

        # Step 3: Move fast pointer k steps ahead
        slow = fast = head
        for _ in range(k):
            fast = fast.next

        # Step 4: Move both until fast reaches last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Step 5: Rotate
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head
        