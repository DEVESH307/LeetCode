# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         distance = []

#         for x, y in points:
#             distance.append((x*x + y*y, x, y))

#         distance.sort(key=lambda x: x[0])

#         result = []
#         for i in range(k):
#             dist, x, y = distance[i]
#             result.append([x, y])

#         return result


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # function to calculate squared distance
        def distance(point):
            x = point[0]
            y = point[1]
            return x*x + y*y

        # sort using the distance function
        points.sort(key=distance)
        return points[:k]