class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush_max(maxHeap, num)
        while k > 1:
            heapq.heappop_max(maxHeap)
            k -= 1
        return maxHeap[0]

