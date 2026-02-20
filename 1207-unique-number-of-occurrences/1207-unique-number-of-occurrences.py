# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         freq = {}

#         for num in arr:
#             freq[num] = freq.get(num, 0) + 1

#         seen = set()

#         for count in freq.values():
#             if count in seen:
#                 return False
#             seen.add(count)

#         return True


# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         freq = {}

#         for num in arr:
#             freq[num] = freq.get(num, 0) + 1

#         occurrences = list(freq.values())
#         unique_occurrences = set(occurrences)

#         return len(occurrences) == len(unique_occurrences)


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for val in arr:
            freq[val] = freq.get(val, 0) + 1

        # for key, val in freq.items():
        return len(freq.values()) == len(set(freq.values()))