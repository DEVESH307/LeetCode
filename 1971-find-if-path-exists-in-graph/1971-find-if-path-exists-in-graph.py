from collections import defaultdict, deque

class Solution:
    def validPath(self, n, edges, source, destination):

        # Build graph (UNDIRECTED — don't mess this up)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # -------- BFS --------
        def bfs(start, target):
            queue = deque([start])
            visited = set([start])

            while queue:
                node = queue.popleft()

                if node == target:
                    return True

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

            return False

        # -------- DFS (iterative) --------
        def dfs_iter(start, target):
            stack = [start]
            visited = set([start])

            while stack:
                node = stack.pop()

                if node == target:
                    return True

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

            return False

        # -------- DFS (recursive) --------
        visited = set()

        def dfs_rec(node):
            if node == destination:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    if dfs_rec(nei):
                        return True

            return False

        # Choose one
        # return dfs_iter(source, destination)
        # return dfs_rec(source)
        return bfs(source, destination)