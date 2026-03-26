# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1

        lenB = 0
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1

         # align both lists            
        curA, curB = headA, headB

        if lenA > lenB:
            for _ in range(lenA-lenB):
                curA = curA.next
        else:
            for _ in range(lenB-lenA):
                curB = curB.next

        # find intersection
        while curA != curB:
            curA = curA.next
            curB = curB.next

        return curA