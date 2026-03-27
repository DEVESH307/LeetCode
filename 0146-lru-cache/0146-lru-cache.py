class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # dummy node
        self.head = ListNode(0, 0) # LRU side
        self.tail = ListNode(0, 0) # MRU side

        self.head.next = self.tail
        self.tail.prev = self.head

    # insert at tail (most recently used)
    def insert(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    # remove node
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node   
        
    # @return an integer
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val   

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = ListNode(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # remove LRU
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)