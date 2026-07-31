class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, start: int) -> int:
        result = [float('inf')]*(n+1)
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        # print(adj)

        result[start] = 0
        minHeap = []
        heapq.heappush(minHeap, (0, start))
        while len(minHeap):
            t, u = heapq.heappop(minHeap)
            if t > result[u]:
                continue
            for v, dt in adj[u]:
                new_t = t + dt
                if new_t < result[v]:
                    result[v] = new_t
                    # print(result)
                    heapq.heappush(minHeap, (new_t, v))  

        result = result[1:]
        return -1 if max(result) == float('inf') else max(result) 
        