# reverse pairs count using merge sort
class Solution:
    # merge two sorted section
    def merge(self, arr, left, mid, right):
        i, j = left, mid
        temp = []

        while i < mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        # remaining elements
        temp.extend(arr[i:mid]) 
        temp.extend(arr[j:right+1])

        # copy back to original array
        arr[left: right+1] = temp 

    # count total reverse pairs in a section
    def countPairs(self, arr, left, mid, right):
        count  = 0
        j = mid

        for i in range(left, mid):
            while j <= right and arr[i] > 2 * arr[j]:
                j += 1
            count += (j - mid)

        return count

    # merge sort + count reverse pairs
    def countReversePairs(self, arr, left, right):
        if left >= right:
            return 0

        mid = (left+right)//2
        count = self.countReversePairs(arr, left, mid)
        count += self.countReversePairs(arr, mid+1, right)
        # count before merge
        count += self.countPairs(arr, left, mid+1, right)
        # normal merge
        self.merge(arr, left, mid + 1, right)
        
        return count

    # main function
    def reversePairs(self, nums: List[int]) -> int:
        return self.countReversePairs(nums, 0, len(nums)-1)
        