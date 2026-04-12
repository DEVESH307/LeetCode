# class TrieNode:
#     def __init__(self):
#         self.children = [None, None]

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, num):
#         node = self.root
#         for i in range(31, -1, -1):
#             bit = (num >> i) & 1
#             if not node.children[bit]:
#                 node.children[bit] = TrieNode()
#             node = node.children[bit]

#     def max_xor(self, num):
#         node = self.root
#         ans = 0

#         for i in range(31, -1, -1):
#             bit = (num >> i) & 1
#             opp = 1 - bit

#             if node.children[opp]:
#                 ans |= (1 << i)
#                 node = node.children[opp]
#             else:
#                 node = node.children[bit]

#         return ans

# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         trie = Trie()
#         max_xor = 0

#         for num in nums:
#             trie.insert(num)

#         ans = 0
#         for num in nums:
#             ans = max(ans, trie.max_xor(num))

#         return ans


# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)

#         ans = 0
#         for i in range(n):
#             for j in range(i + 1, n):
#                 ans = max(ans, nums[i] ^ nums[j])

#         return ans


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0

        for i in range(30, -1, -1):
            mask |= (1 << i)

            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)

            candidate = max_xor | (1 << i)

            for p in prefixes:
                if (p ^ candidate) in prefixes:
                    max_xor = candidate
                    break

        return max_xor