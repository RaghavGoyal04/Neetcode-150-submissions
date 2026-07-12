class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        freqs = Counter(nums)
        for key, v in freqs.items():
            heapq.heappush(minHeap, (v, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        while len(minHeap):
            res.append(heapq.heappop(minHeap)[1])
        return res

        