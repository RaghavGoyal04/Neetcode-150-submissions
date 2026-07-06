class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            first, second = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            if first > second:
                diff = first - second
                heapq.heappush(maxHeap, -diff)
        return -maxHeap[0] if len(maxHeap) else 0


        