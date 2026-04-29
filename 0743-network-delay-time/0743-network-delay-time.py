# from collections import defaultdict
# import heapq

# class Solution:
#     def networkDelayTime(self, times, n, k):
#         graph = defaultdict(list)

#         # directed graph
#         for u, v, w in times:
#             graph[u].append((v, w))

#         dist = [float('inf')] * (n + 1)
#         dist[k] = 0

#         heap = [(0, k)]

#         while heap:
#             d, node = heapq.heappop(heap)

#             if d > dist[node]:
#                 continue

#             for nei, w in graph[node]:
#                 if d + w < dist[nei]:
#                     dist[nei] = d + w
#                     heapq.heappush(heap, (dist[nei], nei))

#         # check unreachable
#         if any(dist[i] == float('inf') for i in range(1, n+1)):
#             return -1

#         return max(dist[1:])


from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        # build directed graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # distance array (1-based)
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]
        max_time = 0

        while heap:
            d, node = heapq.heappop(heap)

            # skip outdated entries
            if d > dist[node]:
                continue

            # # track max distance seen so far
            # max_time = max(max_time, d)

            for nei, w in graph[node]:
                if d + w < dist[nei]:
                    dist[nei] = d + w
                    heapq.heappush(heap, (dist[nei], nei))

        # check if any node is unreachable
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            else:
                max_time = max(max_time, dist[i])

        return max_time