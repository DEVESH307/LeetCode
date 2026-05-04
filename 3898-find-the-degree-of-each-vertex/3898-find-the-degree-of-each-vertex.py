# class Solution:
#     def findDegrees(self, matrix: list[list[int]]) -> list[int]:
#         n = len(matrix)
#         degree = [0] * n

#         for i in range(n):
#             for j in range(n):
#                 if matrix[i][j] == 1:
#                     degree[i] += 1

#         return degree


class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        degree = []

        for item in matrix:
            degree.append(sum(item))

        return degree