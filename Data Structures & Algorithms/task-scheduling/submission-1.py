class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks) #O(M); M <- len(tasks)
        maxHeap = []
        for k, v in freqs.items(): #O(klogk) ; k <= 26 -> O(1)
            heapq.heappush_max(maxHeap, (v, k))
        
        time = 0
        #TC: O(M) since every frequency sums upto M
        #SC: O(26)
        while len(maxHeap): 
            temp = {}
            i = 1
            #After picking 1st task I can complete another 'n' tasks 
            while i <= n+1 and len(maxHeap):
                count, task = heapq.heappop_max(maxHeap)
                if count - 1 > 0:
                    temp[task] = count-1
                i += 1
            
            # Push remaining tasks back into the heap
            for k, v in temp.items():
                heapq.heappush_max(maxHeap, (v, k))

            # If the heap is empty, this was the last batch. 
            # We don't have idle time at the end.
            # Add the exact number of tasks we processed in this batch (which is i - 1).
            if len(maxHeap) == 0:
                time += i - 1
            else:
                # Otherwise, we had to take the full n+1 cycle length (including idles)
                time += n + 1

        return time
        