from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()

        for i in range(k):
            while dq and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])

        for i in range(k, len(nums)):
            result.append(dq[0])

            if dq and nums[i-k] == dq[0]:
                dq.popleft()

            while dq and nums[i] > dq[-1]:
                dq.pop()

            dq.append(nums[i])

        result.append(dq[0])
        return result