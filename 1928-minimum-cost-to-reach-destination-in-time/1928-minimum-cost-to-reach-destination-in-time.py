from collections import defaultdict
import heapq

class Solution:
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)

        # build graph
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # min heap → (cost, time, node)
        heap = [(passingFees[0], 0, 0)]

        # best time to reach each node
        best_time = [float('inf')] * n
        best_time[0] = 0

        while heap:
            cost, time, node = heapq.heappop(heap)

            # reached destination
            if node == n - 1:
                return cost

            for nei, t in graph[node]:
                new_time = time + t
                new_cost = cost + passingFees[nei]

                if new_time > maxTime:
                    continue

                # only push if we improved time
                if new_time < best_time[nei]:
                    best_time[nei] = new_time
                    heapq.heappush(heap, (new_cost, new_time, nei))

        return -1