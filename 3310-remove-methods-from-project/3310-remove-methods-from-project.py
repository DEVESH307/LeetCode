# from collections import defaultdict, deque

# class Solution:
#     def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:

#         # 1. Build directed adjacency graph
#         adj = defaultdict(list)

#         for u, v in invocations:
#             adj[u].append(v)

#         # 2. BFS from k → find all suspicious methods
#         suspicious = set([k])
#         queue = deque([k])

#         while queue:
#             node = queue.popleft()

#             for nei in adj[node]:
#                 if nei not in suspicious:
#                     suspicious.add(nei)
#                     queue.append(nei)

#         # 3. Check: safe → suspicious edge
#         for u, v in invocations:
#             if u not in suspicious and v in suspicious:
#                 return list(range(n))

#         # 4. Return non-suspicious methods
#         ans = []

#         for method in range(n):
#             if method not in suspicious:
#                 ans.append(method)

#         return ans
        
        
        
from collections import defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:

        # 1. Build directed adjacency graph
        adj = defaultdict(list)

        for u, v in invocations:
            adj[u].append(v)

        # 2. Find all suspicious methods using DFS
        suspicious = set()

        def dfs(node):
            suspicious.add(node)

            for nei in adj[node]:
                if nei not in suspicious:
                    dfs(nei)

        dfs(k)

        # 3. Check if any SAFE method calls a SUSPICIOUS method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # Cannot remove suspicious methods
                return list(range(n))

        # 4. Otherwise remove suspicious methods
        ans = []

        for method in range(n):
            if method not in suspicious:
                ans.append(method)

        return ans