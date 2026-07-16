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
            # 1. Take the current number
            path.append(nums[i])
            backtrack(i+1, path)

            #undo
            path.pop()

            # 2. Don't take the current number (and skip duplicates)
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, path)

        backtrack(0, [])
        return res