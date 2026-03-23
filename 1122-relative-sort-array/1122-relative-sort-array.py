class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}

        for i, num in enumerate(arr1):
            freq[num] = freq.get(num, 0) + 1

        arr1.clear()
        for i, num in enumerate(arr2):
            if num in freq:
                arr1.extend([num] * freq[num])
                del freq[num]

        for num in sorted(freq):
            arr1.extend([num] * freq[num])
            del freq[num]

        return arr1
