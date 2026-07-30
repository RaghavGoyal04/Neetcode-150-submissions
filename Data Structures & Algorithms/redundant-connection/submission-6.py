class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            u = q.popleft()
            indegree[u] -= 1
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 1:
                    q.append(v)

        # print(indegree)

        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]

        return []
