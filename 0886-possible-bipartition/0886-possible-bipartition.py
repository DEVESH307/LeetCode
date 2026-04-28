class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # build graph
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = [-1] * (n + 1)  # -1 = unvisited
        for v in range(1, n+1):
            if color[v] != -1:
                continue
            queue = deque([v])
            color[v] = 1

            while queue:
                node = queue.popleft()

                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        queue.append(nei)
                    else:
                        if color[nei] == color[node]:
                            return False # conflict → not bipartite

        return True        