import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        min_heap = []
        res = []
        seen = set()

        heapq.heappush(min_heap, (nums1[0] + nums2[0], 0, 0))
        seen.add((0, 0))

        for _ in range(k):
            # if not min_heap:
            #     break

            val, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                heapq.heappush(min_heap, (nums1[i+1] + nums2[j], i+1, j))
                seen.add((i+1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
                seen.add((i, j+1))

        return res