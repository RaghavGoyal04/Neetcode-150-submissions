class MedianFinder:
    def __init__(self):
        #to store right bound values; for odd length this will give median
        #for even length, we get first value from minHeap and first value from maxHeap 
        #and then calculate the median 
        self.maxHeap_l = []
        self.minHeap_r = [] 
         
    def addNum(self, num: int) -> None:
        if self.maxHeap_l and num < self.maxHeap_l[0]:
            heapq.heappush_max(self.maxHeap_l, num)
        else:
            heapq.heappush(self.minHeap_r, num)

        if len(self.minHeap_r) > len(self.maxHeap_l) + 1:
            temp = heapq.heappop(self.minHeap_r)
            heapq.heappush_max(self.maxHeap_l, temp)

        if len(self.maxHeap_l) > len(self.minHeap_r) + 1:
            temp = heapq.heappop_max(self.maxHeap_l)
            heapq.heappush(self.minHeap_r, temp)

    def findMedian(self) -> float:
        print(self.maxHeap_l, self.minHeap_r)
        if len(self.maxHeap_l) > len(self.minHeap_r):
            return 1.0 * (self.maxHeap_l[0])
        elif len(self.maxHeap_l) < len(self.minHeap_r):
            return 1.0 * (self.minHeap_r[0])
        else: # even
            return 1.0 * (self.maxHeap_l[0] + self.minHeap_r[0]) / 2
        
        