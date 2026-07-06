class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.capacity = k
        for i in nums:
            heapq.heappush(self.minHeap, i)
            if len(self.minHeap) > self.capacity: 
                temp = heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.capacity: 
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
