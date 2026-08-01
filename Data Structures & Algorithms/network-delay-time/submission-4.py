class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(set)
        result = {i: float('inf') for i in range(1, n+1)}
        result[k] = 0
        for u, v, t in times:
            adj[u].add((v, t))
        
        # print(result, adj)

        minheap = []
        heapq.heappush(minheap, (0, k))
        while len(minheap):
            t, u = heapq.heappop(minheap)
            # print(u, t)
            if t > result[u]:
                continue
            for v, dt in adj[u]:
                new_t = t + dt
                if new_t < result[v]:
                    result[v] = new_t
                    heapq.heappush(minheap, (new_t, v))
        
        return -1 if max(result.values()) == float('inf') else max(result.values())
