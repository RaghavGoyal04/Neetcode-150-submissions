class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        
        res = []
        nums.sort()
        def backtrack(i, path):
            if i >= len(nums):
                res.append(path[:])
                return
            
            #take 
            backtrack(i+1, path + [nums[i]])
            #not take while i+1 != i
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, path)

        backtrack(0, [])
        return res
        
# [1,1,2]
# take:
# [1]
#     take: [1,1]   not_take: []

# not take:
# []