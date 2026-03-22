# class Solution:
#     def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
#         MOD = 10**9+7
#         n = len(nums)
#         subarr_sum = []
        
#         for i in range(n):
#             total = 0
#             for j in range(i, n):
#                 total += nums[j]
#                 subarr_sum.append(total)

#         subarr_sum.sort()
#         return sum(subarr_sum[left-1:right]) % MOD


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        
        # prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        # prefix of prefix (for fast sum calc)
        prefix2 = [0] * (n + 1)
        for i in range(n):
            prefix2[i+1] = prefix2[i] + prefix[i+1]
        
        # count subarrays with sum <= target
        def count_and_sum(target):
            count = 0
            total_sum = 0
            j = 0
            
            for i in range(n):
                while j < n and prefix[j+1] - prefix[i] <= target:
                    j += 1
                
                count += (j - i)
                
                # sum of subarrays starting at i
                total_sum += (prefix2[j] - prefix2[i]) - prefix[i] * (j - i)
            
            return count, total_sum
        
        # get sum of first k smallest subarray sums
        def kth_sum(k):
            lo, hi = 0, prefix[-1]
            
            while lo < hi:
                mid = (lo + hi) // 2
                count, _ = count_and_sum(mid)
                
                if count < k:
                    lo = mid + 1
                else:
                    hi = mid
            
            count, total = count_and_sum(lo)
            return total - lo * (count - k)
        
        return (kth_sum(right) - kth_sum(left - 1)) % MOD