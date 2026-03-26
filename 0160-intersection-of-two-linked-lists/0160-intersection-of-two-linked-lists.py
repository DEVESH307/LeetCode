# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         lenA = 0
#         cur = headA
#         while cur:
#             cur = cur.next
#             lenA += 1

#         lenB = 0
#         cur = headB
#         while cur:
#             cur = cur.next
#             lenB += 1

#          # align both lists            
#         curA, curB = headA, headB

#         if lenA > lenB:
#             for _ in range(lenA-lenB):
#                 curA = curA.next
#         else:
#             for _ in range(lenB-lenA):
#                 curB = curB.next

#         # find intersection
#         while curA != curB:
#             curA = curA.next
#             curB = curB.next

#         return curA


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1