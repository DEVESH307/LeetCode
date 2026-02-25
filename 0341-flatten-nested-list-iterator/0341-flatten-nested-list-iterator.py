# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.flist = []
#         self.index = 0
#         self.flattenList(nestedList)

#     def flattenList(self, nestedList):
#         for item in nestedList:
#             if item.isInteger():
#                 self.flist.append(item.getInteger())
#             else:
#                 self.flattenList(item.getList())


#     def next(self):
#         val = self.flist[self.index]
#         self.index += 1
#         return val


#     def hasNext(self):
#         return self.index < len(self.flist)
        

# # Your NestedIterator object will be instantiated and called as such:
# # i, v = NestedIterator(nestedList), []
# # while i.hasNext(): v.append(i.next())



class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
    

    def next(self):
        return self.stack.pop().getInteger()


    def hasNext(self):
        while self.stack:
            top = self.stack[-1]

            if top.isInteger():
                return True

            self.stack.pop()
            self.stack.extend(top.getList()[::-1])

        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())