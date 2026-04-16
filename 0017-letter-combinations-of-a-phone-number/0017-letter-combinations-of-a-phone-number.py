# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
        
#         mapping = {
#             '0': '0',
#             '1': '1',
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }
        
#         result = []
        
#         def dfs(index, path):
#             # base case
#             if index == len(digits):
#                 result.append(path)
#                 return
            
#             for char in mapping[digits[index]]:
#                 dfs(index + 1, path + char)
        
#         dfs(0, "")
        
#         return sorted(result)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            '0': '0',
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        path = [''] * len(digits)   # preallocate
        
        def dfs(index):
            if index == len(digits):
                result.append(''.join(path))
                return
            
            for char in mapping[digits[index]]:
                path[index] = char
                dfs(index + 1)
        
        dfs(0)
        return result