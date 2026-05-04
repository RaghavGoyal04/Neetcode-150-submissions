class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        # seen = [-1]*(n+1)
        # for i in range(n):
        #     if seen[nums[i]] == 1:
        #         return nums[i]
        #     seen[nums[i]] = 1
        
        #find duplicate
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f: 
                break 
            

        l = 0
        while True:
            l = nums[l]
            s = nums[s]
            if l == s: 
                return s
            
