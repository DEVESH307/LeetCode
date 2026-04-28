from collections import defaultdict, deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        
        def bfs():
            # final state: all nodes visited
            final_mask = (1 << n) - 1

            visited = set() 
            queue = deque()

            # multi-source start
            for i in range(n):
                mask = 1 << i
                queue.append((i, mask, 0)) # (node, mask, distance)
                visited.add((i, mask))

            while queue:
                node, mask, dist = queue.popleft()

                if mask == final_mask:
                    return dist

                for nei in graph[node]:
                    new_mask = mask | (1 << nei)

                    if (nei, new_mask) not in visited:
                        visited.add((nei, new_mask))
                        queue.append((nei, new_mask, dist + 1))

        return bfs()