class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #using dfs for cycle detection
        adj = defaultdict(set)
        for v, u in prerequisites:
            adj[u].add(v)

        self.visited = [False] * numCourses
        self.rec_path = [False] * numCourses
        
        def has_cycle(u):
            self.visited[u] = True
            self.rec_path[u] = True
            for v in adj[u]:
                if not self.visited[v] and has_cycle(v):
                    return True
                if self.rec_path[v]:
                    return True
            self.rec_path[u] = False
            return False
        
        for u in range(numCourses):
            if not self.visited[u] and has_cycle(u):
                return False
        
        return True