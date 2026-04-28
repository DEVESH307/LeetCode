# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         n = len(graph)
#         color = [-1] * n  # -1 = unvisited
#         for v in range(n):
#             if color[v] != -1:
#                 continue
#             queue = deque([v])
#             color[v] = 0

#             while queue:
#                 node = queue.popleft()

#                 for nei in graph[node]:
#                     if color[nei] == -1:
#                         color[nei] = 1 - color[node]
#                         queue.append(nei)
#                     else:
#                         if color[nei] == color[node]:
#                             return False # conflict → not bipartite

#         return True           


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        color = [-1] * n  # -1 = unvisited

        def dfs(node, c):
            color[node] = c

            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, 1 - c):
                        return False
                elif color[nei] == c:
                    return False  # same color → odd cycle

            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False  # odd cycle exists

        return True  # no odd cycle → bipartite