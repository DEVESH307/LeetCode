# class Solution:
#     def lexicalOrder(self, n: int) -> list[int]:
#         ans = []

#         def dfs(curr):
#             if curr > n:
#                 return

#             ans.append(curr)

#             for digit in range(10):
#                 nxt = curr * 10 + digit

#                 if nxt > n:
#                     break

#                 dfs(nxt)

#         for start in range(1, 10):
#             if start > n:
#                 break

#             dfs(start)

#         return ans


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        curr = 1
        
        for _ in range(n):
            ans.append(curr)
            
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10

                curr += 1

        return ans