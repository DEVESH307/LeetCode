# class Solution:
#     # @param triangle : list of list of integers
#     # @return an integer
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         m =len(triangle)
#         n =len(triangle[0])

#         def dfs(i, j):
#             if i >= m or j < 0 or j >= len(triangle[i]):
#                 return float('inf')
                
#             # last row
#             if i == m - 1:
#                 return triangle[i][j]

#             return triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))

#         return dfs(0, 0)


# class Solution:
#     # @param triangle : list of list of integers
#     # @return an integer
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         m =len(triangle)
#         n =len(triangle[0])
#         dp = [[-1] * len(row) for row in triangle]

#         def dfs(i, j):
#             # last row
#             if i == m - 1:
#                 return triangle[i][j]
            
#             if dp[i][j] != -1:
#                 return dp[i][j]

#             dp[i][j] = triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
#             return dp[i][j]

#         return dfs(0, 0)


# class Solution:
#     # @param triangle : list of list of integers
#     # @return an integer
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         m =len(triangle)
#         n =len(triangle[0])
#         dp = [[0] * len(row) for row in triangle]
        
#         # base case → last row
#         for j in range(len(triangle[m-1])):
#             dp[m-1][j] = triangle[m-1][j]

#         for i in range(m - 2, -1, -1):
#             for j in range(len(triangle[i])):
#                 dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
            
#         return dp[0][0]


class Solution:
    # @param triangle : list of list of integers
    # @return an integer
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m =len(triangle)
        n =len(triangle[0])
        dp = [[0] * len(row) for row in triangle]
        
        # start from last row
        dp = triangle[-1][:]

        # move upwards
        for i in range(m - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
            
        return dp[0]