class Solution:
    def nearestGreaterOnRight(self, arr):
        n = len(arr)
        stack = []
        nge_map = {}

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            if stack:
                nge_map[arr[i]] = arr[stack[-1]]
            else:
                nge_map[arr[i]] = -1

            stack.append(i)

        return nge_map


    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge_map = self.nearestGreaterOnRight(nums2)
        return [nge_map[num] for num in nums1]