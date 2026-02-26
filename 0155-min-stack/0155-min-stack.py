class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self) -> None:
        if not self.stack:
            return

        top = self.stack.pop()
        
        if top == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self) -> int:
        return -1 if not self.stack else self.stack[-1]        


    def getMin(self) -> int:
        return -1 if not self.min_stack else self.min_stack[-1]  


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()