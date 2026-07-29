class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        n = len(edges)
        
        def dfs(u, par):
            visited.add(u)
            for v in adj[u]:
                if v == par:
                    continue

                if v in visited or dfs(v, u):
                    return True
                
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()
            
            if dfs(u, -1):
                return [u, v]
        
        return []
        

        

