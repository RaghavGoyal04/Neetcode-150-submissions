class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegrees = [0]*numCourses
        for v, u in prerequisites:
            adj[u].append(v)
            indegrees[v] += 1
        q = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        res = []
        while q:
            u = q.popleft()
            numCourses -= 1
            for v in adj[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
            res.append(u)
        # print(res)
        return res if not numCourses else []

