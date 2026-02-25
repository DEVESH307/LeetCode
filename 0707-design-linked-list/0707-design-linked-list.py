# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next 


# class MyLinkedList:

#     def __init__(self):
#         self.node = ListNode(0) #fake head
#         self.size = 0
        

#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.size:
#             return -1
        
#         curr = self.node.next

#         for _ in range(index):
#             curr = curr.next

#         return curr.val
        

#     def addAtHead(self, val: int) -> None:
#         self.addAtIndex(0, val)
        

#     def addAtTail(self, val: int) -> None:
#         self.addAtIndex(self.size, val)


#     def addAtIndex(self, index: int, val: int) -> None:
#         if index < 0 or index > self.size:
#             return

#         prev = self.node

#         for _ in range(index):
#             prev = prev.next

#         new_node = ListNode(val)
#         new_node.next = prev.next
#         prev.next = new_node

#         self.size += 1
        

#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:
#             return

#         prev = self.node

#         for _ in range(index):
#             prev = prev.next

#         prev.next = prev.next.next
#         self.size -= 1
        

# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)



class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        # dummy head and tail
        self.head = ListNode(0)
        self.tail = ListNode(0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0


    # ---------- INTERNAL HELPER ----------
    # get node at index
    def getNode(self, index):

        # choose shortest direction
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - index - 1):
                curr = curr.prev

        return curr


    # ---------- GET ----------
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        node = self.getNode(index)
        return node.val


    # ---------- ADD AT HEAD ----------
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    # ---------- ADD AT TAIL ----------
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    # ---------- ADD AT INDEX ----------
    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index > self.size:
            return

        # node that will come after new node
        if index == self.size:
            nxt = self.tail
        else:
            nxt = self.getNode(index)

        prev = nxt.prev

        new_node = ListNode(val)

        # connect 4 pointers
        new_node.prev = prev
        new_node.next = nxt

        prev.next = new_node
        nxt.prev = new_node

        self.size += 1


    # ---------- DELETE ----------
    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:
            return

        node = self.getNode(index)

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1