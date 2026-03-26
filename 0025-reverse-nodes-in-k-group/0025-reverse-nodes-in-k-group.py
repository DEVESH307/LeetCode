# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseFirstKNodes(self, head, k):
#         if not head or k <= 1:
#             return head

#         # check if k nodes exist
#         temp = head
#         count = 0
#         while temp and count < k:
#             temp = temp.next
#             count += 1

#         if count < k:
#             return head  # no reversal

#         head2 = None
#         next_node = head

#         while k > 0 and next_node:
#             temp = next_node
#             next_node = next_node.next
#             temp.next = head2
#             head2 = temp
#             k -= 1

#         head.next = next_node # connect tail of reversed part
#         return head2 # new head of this segment


#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if not head or k <= 1:
#             return head

#         new_head = self.reverseFirstKNodes(head, k)

#         # head is now the tail of the reversed block
#         head.next = self.reverseKGroup(head.next, k)

#         return new_head
    


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseFirstKNodes(self, head, k):
        if not head or k <= 1:
            return head

        # check if k nodes exist
        temp = head
        count = 0
        while temp and count < k:
            temp = temp.next
            count += 1

        if count < k:
            return head, None  # no reversal

        head2 = None
        next_node = head

        while k > 0 and next_node:
            temp = next_node
            next_node = next_node.next
            temp.next = head2
            head2 = temp
            k -= 1

        head.next = next_node # connect tail of reversed part
        return head2, next_node # return new head + next segment start


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev_tail = dummy
        cur = head

        while cur:
            # reverse next k nodes
            new_head, next_segment = self.reverseFirstKNodes(cur, k)

            # connect previous part to reversed segment
            prev_tail.next = new_head

            # current node becomes tail after reversal
            prev_tail = cur

            # move to next segment
            cur = next_segment

        return dummy.next
        