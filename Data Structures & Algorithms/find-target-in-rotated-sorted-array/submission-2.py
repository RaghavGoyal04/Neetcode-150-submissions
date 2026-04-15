class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        res = -1
        while l <= r:
            m = (l+r)//2
            # print(l, r, m)
            if nums[m] == target:
                res = m
                return res
            
            #left half sorted 
            if nums[l] <= nums[m]:
                if nums[l] > target or nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            else:
            #right half sorted 
                if nums[r] < target or nums[m] > target:
                    r = m-1
                else:
                    l = m+1 
        return res


        