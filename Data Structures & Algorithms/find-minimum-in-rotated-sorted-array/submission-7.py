class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

        # res = float('inf')
        # while l <= r:
        #     m = l + (r-l)//2
        #     res = min(res, nums[m])
            
        #     # if m itself is pivot
        #     if ((m == 0 and nums[m] < nums[m+1]) or (m == n-1 and nums[m-1] > nums[m]) or (nums[m-1] > nums[m] < nums[m+1])):
        #         return nums[m]
            
        #     if (nums[m-1] < nums[m] > nums[m+1]):
        #         res = min(nums[m], nums[m-1], nums[m+1])
        #         return res 
        #     elif nums[l] < nums[m]:
        #         #left section sorted
        #         if nums[l] < nums[r]:
        #             r = m-1
        #         else:
        #             l = m+1
        #     else:
        #         #right section sorted
        #         if nums[l] < nums[r]:
        #             l = m+1
        #         else:
        #             r = m-1
        # return res
        

        