class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        st = set()

        for i in range(n-1):
            sum = nums[i] + nums[i+1]

            if sum in st:
                return True
            else:
                st.add(sum)

        return False
        