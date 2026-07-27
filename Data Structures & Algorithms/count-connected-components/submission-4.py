class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        visited = [False]*n
        
        connected = 0
        for i in range(n):
            if not visited[i]:
                q = deque([i])
                while q:
                    u = q.popleft()
                    visited[u] = True
                    for v in adj[u]:
                        if not visited[v]:
                            q.append(v)
                connected += 1

        return connected