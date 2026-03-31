# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_stack = []


#     def push(self, val: int) -> None:
#         self.stack.append(val)
        
#         if not self.min_stack or val <= self.min_stack[-1]:
#             self.min_stack.append(val)


#     def pop(self) -> None:
#         if not self.stack:
#             return

#         top = self.stack.pop()
        
#         if top == self.min_stack[-1]:
#             self.min_stack.pop()


#     def top(self) -> int:
#         return -1 if not self.stack else self.stack[-1]        


#     def getMin(self) -> int:
#         return -1 if not self.min_stack else self.min_stack[-1]  


# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(val)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None


    def push(self, val: int) -> None:
        # If stack is empty, initialize min and push value
        if not self.stack:
            self.stack.append(val)
            self.min_val = val
        # If val is greater or equal, push normally
        elif val >= self.min_val:
            self.stack.append(val)
        else:
            # Encode value to store previous min implicitly
            self.stack.append(2 * val - self.min_val)
            # Update min to new value
            self.min_val = val


    def pop(self) -> None:
        # Do nothing if stack is empty
        if not self.stack:
            return

        top = self.stack.pop()
            
        # If popped value is encoded, restore previous min
        if top < self.min_val:
            self.min_val = 2 * self.min_val - top


    def top(self) -> int:
        # Return -1 if empty
        if not self.stack:
            return -1

        top = self.stack[-1]

        # If encoded value, actual top is current min
        if top < self.min_val:
            return self.min_val

        return top


    def getMin(self) -> int:
        # Return -1 if empty, else current min
        return -1 if not self.stack else self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()