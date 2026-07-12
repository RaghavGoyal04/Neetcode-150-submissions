class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks) #O(M); M <- len(tasks)
        time = 0

        # maxHeap = []
        # for k, v in freqs.items(): #O(klogk) ; k <= 26 -> O(1)
        #     heapq.heappush_max(maxHeap, (v, k))

        #TC: O(M) since every frequency sums upto M
        #SC: O(26)
        # while len(maxHeap): 
        #     temp = {}
        #     i = 1
        #     #After picking 1st task I can complete another 'n' tasks 
        #     while i <= n+1 and len(maxHeap):
        #         count, task = heapq.heappop_max(maxHeap)
        #         if count - 1 > 0:
        #             temp[task] = count-1
        #         i += 1
            
        #     # Push remaining tasks back into the heap
        #     for k, v in temp.items():
        #         heapq.heappush_max(maxHeap, (v, k))

        #     # If the heap is empty, this was the last batch. 
        #     # We don't have idle time at the end.
        #     # Add the exact number of tasks we processed in this batch (which is i - 1).
        #     if len(maxHeap) == 0:
        #         time += i - 1
        #     else:
        #         # Otherwise, we had to take the full n+1 cycle length (including idles)
        #         time += n + 1


        #using queue to maintain the time
        # queue will hold (frequency, exection time)
        # exection time : current_time + cool_down time
        maxHeap = []
        for _, v in freqs.items(): #O(klogk) ; k <= 26 -> O(1)
            heapq.heappush_max(maxHeap, v)
        q = deque()
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1 #processing the task
                if cnt:
                    q.append([cnt, time + n])
            else:
                #nothing left in the maxHeap
                time = q[0][1]

            #if there's something in the queue, push it back to maxHeap
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])

        return time
        