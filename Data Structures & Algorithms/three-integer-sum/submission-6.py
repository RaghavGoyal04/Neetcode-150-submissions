class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # 1. Optimization: If the smallest number is > 0, no triplet can sum to 0
            if nums[i] > 0: break

            # 2.Skip duplicate pivots
            if i > 0 and nums[i] == nums[i-1]: continue 
            

            l, r = i+1, len(nums)-1
            while l < r :
                # if l > i+1 and nums[l] == nums[l-1]:
                #     l += 1
                #     continue
                # if r < len(nums)-1  and nums[r] == nums[r+1]:
                #     r -= 1
                #     continue
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # Move pointers and SKIP duplicates here
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1 
                elif  nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1 
        return res
        