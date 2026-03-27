class ListNode:
    def __init__(self, key, val):
        # Each node stores:
        # key → needed for deletion from hashmap
        # val → actual value
        # freq → how many times accessed
        self.key = key
        self.val = val
        self.freq = 1  # new node always starts with frequency = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        # Dummy head & tail to avoid edge-case checks
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        # Insert node at the tail (MRU position)
        # Why tail? → within same frequency, we maintain LRU order
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        # Remove node from DLL in O(1)
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def pop_lru(self):
        # Remove least recently used node (head.next)
        # This is used during eviction when multiple nodes have same freq
        if self.head.next == self.tail:
            return None  # empty list
        lru = self.head.next
        self.remove(lru)
        return lru

    def is_empty(self):
        # Check if DLL has no real nodes
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        # Maximum number of keys allowed
        self.capacity = capacity

        # key_map: key → node
        # Gives O(1) access to any key
        self.key_map = {}

        # freq_map: freq → DLL of nodes
        # Groups nodes by frequency
        # Each DLL maintains LRU order within that frequency
        self.freq_map = {}

        # Tracks minimum frequency currently present in cache
        # This is CRITICAL for O(1) eviction
        self.min_freq = 0

    def update_freq(self, node):
        """
        This is the CORE of LFU.

        Whenever a node is accessed:
        1. Remove it from its current frequency list
        2. Increase its frequency
        3. Insert it into new frequency list
        """

        freq = node.freq

        # Remove node from current freq list
        self.freq_map[freq].remove(node)

        # If this node was the ONLY node in min_freq bucket,
        # and we remove it → min_freq must increase
        if freq == self.min_freq and self.freq_map[freq].is_empty():
            self.min_freq += 1

        # Increase frequency
        node.freq += 1

        # Add node to new frequency list
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DLL()

        self.freq_map[node.freq].insert(node)

    def get(self, key: int) -> int:
        """
        Return value if key exists, else -1.
        Also update frequency because access counts.
        """

        if key not in self.key_map:
            return -1

        node = self.key_map[key]

        # Access → frequency increases
        self.update_freq(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key.

        Rules:
        - If key exists → update value + frequency
        - If cache full → evict LFU
        - New node always starts with freq = 1
        """

        if self.capacity == 0:
            return  # edge case

        # Case 1: key already exists → update value + freq
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self.update_freq(node)
            return

        # Case 2: cache full → evict LFU
        if len(self.key_map) >= self.capacity:
            # Find the lowest frequency bucket
            lfu_list = self.freq_map[self.min_freq]

            # Remove LRU node from that bucket
            node_to_remove = lfu_list.pop_lru()

            # Remove from hashmap
            del self.key_map[node_to_remove.key]

        # Insert new node
        new_node = ListNode(key, value)
        self.key_map[key] = new_node

        # Add to frequency = 1 bucket
        if 1 not in self.freq_map:
            self.freq_map[1] = DLL()

        self.freq_map[1].insert(new_node)

        # IMPORTANT:
        # New node has freq = 1 → min_freq must reset to 1
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)