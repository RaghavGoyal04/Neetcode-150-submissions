class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #kahn algo for topological sort
        adj = defaultdict(set)
        indegrees = [0]*numCourses
        for v, u in prerequisites:
            adj[u].add(v)
            indegrees[v] += 1
        
        q = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            numCourses -= 1
            for v in adj[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        
        return True if not numCourses else False