class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            else:
                q.append(nums[i])

        result.append(q[0])
        for i in range(k, len(nums)):
            if nums[i-k] == q[0]:
                q.popleft()
            while q and q[-1] < nums[i]:
                q.pop()
            else:
                q.append(nums[i])
            
            result.append(q[0])

        return result        