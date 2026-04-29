class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph and indegree list
        graph = defaultdict(list)
        indegree = [0] * (numCourses)
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return len(order) == numCourses