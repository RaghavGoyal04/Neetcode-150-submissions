class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            # At EVERY step, we check all possible numbers
            for i in range(len(nums)):
                if not used[i]:
                    # 1. Choose the number
                    used[i] = True
                    # 2. Explore further with this number included
                    helper(path + [nums[i]], used)
                    # 3. Undo the choice (backtrack) to try the next option
                    used[i] = False


        
        helper([], [False] * len(nums))
        return res