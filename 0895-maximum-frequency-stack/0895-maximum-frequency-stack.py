class FreqStack:

    def __init__(self):
        self.freq_map = {}
        self.freq_stack_map = {}
        self.max_freq = 0


    def push(self, val: int) -> None:
        self.freq_map[val] = self.freq_map.get(val, 0) + 1
        freq = self.freq_map[val]

        if freq not in self.freq_stack_map:
            self.freq_stack_map[freq] = []

        self.freq_stack_map[freq].append(val)
        self.max_freq = max(self.max_freq, freq)


    def pop(self) -> int:
        val = self.freq_stack_map[self.max_freq].pop()
        self.freq_map[val] -= 1

        if not self.freq_stack_map[self.max_freq]:
            del self.freq_stack_map[self.max_freq]
            self.max_freq -= 1

        return val
                


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()