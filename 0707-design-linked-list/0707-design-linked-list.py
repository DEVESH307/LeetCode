class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next 


class MyLinkedList:

    def __init__(self):
        self.node = ListNode(0) #fake head
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.node.next

        for _ in range(index):
            curr = curr.next

        return curr.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        prev = self.node

        for _ in range(index):
            prev = prev.next

        new_node = ListNode(val)
        new_node.next = prev.next
        prev.next = new_node

        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.node

        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next
        self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)