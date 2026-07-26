class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque([(0, -1)]) # (current node, parent node)
        while q:
            u, parent = q.popleft()
            visited.add(u)
            for v in adj[u]:
                if v == parent:
                    continue
                if v in visited:
                    return False
                q.append((v, u))
        
        return len(visited) == n
