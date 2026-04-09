class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k: return [max(nums)]

        res = []
        max_heap = []
        
        for idx, val in enumerate(nums[:k]):
            heapq.heappush(max_heap, (-val, idx))
        
        res.append(-max_heap[0][0])
        # print(f'{res=}')

        for i in range(k, len(nums)):
            w_s, w_e = i-k+1, i
            while max_heap and not (w_s <= max_heap[0][1] <= w_e):
                # print(max_heap[0])
                heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-nums[i], i))
            res.append(-max_heap[0][0])
            # print(f'{res=}')
        return res



