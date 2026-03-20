# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def binarySearch(self, arr, target, left, right, asc):
        while left <= right:
            mid = (left + right) // 2
            val = arr.get(mid)
            
            if val == target:
                return mid
            
            if asc:
                if val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if val < target:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1  
        
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        n = arr.length()
        
        # 1. Find peak
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if arr.get(mid) < arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        
        # 2. Binary search (ascending)
        res = self.binarySearch(arr, target, 0, peak, True)
        if res != -1:
            return res
        
        # 3. Binary search (descending)
        return self.binarySearch(arr, target, peak + 1, n - 1, False)

