class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k: return [max(nums)]

        res = []
        
        # optimal approach: Monotonic deque
        q = deque()
        for i, val in enumerate(nums[:k]):
            while q and nums[q[-1]] < val:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])

        for i in range(k, len(nums)):
            #remove invalid entries from starting
            while q and q[0] < i-k+1:
                q.popleft()

            #remove smaller entries from end
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            #finally add current element
            q.append(i)
            res.append(nums[q[0]])

        return res


        ### sub optimal: Max heap approach O(nlogk)
        # max_heap = []
        
        # # TC: O(klogk)
        # for idx, val in enumerate(nums[:k]):
        #     heapq.heappush(max_heap, (-val, idx))
        
        # res.append(-max_heap[0][0])
        
        # # TC: O((n-k)logk)
        # # push -> clean -> read top
        # for i in range(k, len(nums)):
        #     w_s, w_e = i-k+1, i
        #     heapq.heappush(max_heap, (-nums[i], i))
        #     while not (w_s <= max_heap[0][1] <= w_e):
        #         heapq.heappop(max_heap)
        #     res.append(-max_heap[0][0])
        # return res





