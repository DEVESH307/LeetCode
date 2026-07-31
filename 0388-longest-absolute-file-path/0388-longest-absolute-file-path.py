# class Solution:
#     def lengthLongestPath(self, input: str) -> int:
#         stack = [0]
#         ans = 0

#         for line in input.split('\n'):
#             name = line.lstrip('\t')
#             depth = len(line) - len(name)

#             while len(stack) > depth + 1:
#                 stack.pop()
    
#             if '.' in name:
#                 ans = max(ans, stack[-1] + len(name))
#             else:
#                 stack.append(stack[-1] + len(name) + 1)

#         return ans


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        pathLen = {0: 0}
        ans = 0

        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)

            if '.' in name:
                ans = max(ans, pathLen[depth] + len(name))

            else:
                pathLen[depth + 1] = (pathLen[depth] + len(name) + 1)

        return ans