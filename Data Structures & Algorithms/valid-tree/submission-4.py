class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def has_cycle_dfs(u, parent):
            visited.add(u)
            for v in adj[u]:
                if v == parent:
                    continue
                
                if v in visited or has_cycle_dfs(v, u):
                    return True

        return not has_cycle_dfs(0, -1) and len(visited) == n
