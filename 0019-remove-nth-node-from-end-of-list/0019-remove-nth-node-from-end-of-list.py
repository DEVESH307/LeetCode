# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         if not head:
#             return None

#         # Step 1: find size
#         temp = head
#         size = 0
#         while temp:
#             temp = temp.next
#             size += 1

#         # Step 2: find position from start
#         k = size-n

#         # Step 3: remove head if needed
#         if k <= 0:
#             return head.next

#         temp = head
#         prev = None

#         # Step 4: move to (k-1)th node
#         temp = head
#         for _ in range(k - 1):
#             temp = temp.next

#         # Step 5: delete kth node
#         temp.next = temp.next.next

#         return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # single pass solution
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = fast = dummy

        # move fast n steps ahead
        for _ in range(n):
            if fast.next:
                fast = fast.next
            else:
                # n > len(head)
                return head.next

        # move both till fast reaches end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # delete node
        slow.next = slow.next.next

        return dummy.next