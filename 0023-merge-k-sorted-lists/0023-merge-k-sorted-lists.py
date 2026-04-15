# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # Appraoch 1 (O(n*k))
# class Solution:
#     def mergeTwoLists(self, head1, head2):
#         dummy = ListNode(0)
#         tail = dummy

#         while head1 and head2:
#             if head1.val < head2.val:
#                 tail.next = head1
#                 head1 = head1.next
#             else:
#                 tail.next = head2
#                 head2 = head2.next
#             tail = tail.next

#         tail.next = head1 if head1 else head2

#         return dummy.next  

#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists:
#             return None
#         if len(lists) == 1:
#             return lists[0]

#         return self.mergeTwoLists(lists[0], self.mergeKLists(lists[1:]))


# # Appraoch 2: (O(nlogk))
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists:
#             return None

#         while len(lists) > 1:
#             merged = []

#             for i in range(0, len(lists), 2):
#                 l1 = lists[i]
#                 l2 = lists[i + 1] if i + 1 < len(lists) else None
#                 merged.append(self.mergeTwoLists(l1, l2))

#             lists = merged

#         return lists[0]


# Appraoch 3: (O(nlogk))
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # push first node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next