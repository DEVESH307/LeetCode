class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph and indegree list
        graph = defaultdict(list)
        indegree = [0] * (numCourses)
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        # queue = deque([i for i in range(1, numCourses + 1) if indegree[i] == 0])
        
        # use min-heap instead of queue
        min_heap  = []
        for i in range(numCourses):
            if indegree[i] == 0:
                heapq.heappush(min_heap, i)
        
        order = []

        while min_heap:
            node = heapq.heappop(min_heap)
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    heapq.heappush(min_heap ,nei)

        return order if len(order) == numCourses else []