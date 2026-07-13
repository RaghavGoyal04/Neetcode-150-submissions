class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, path, summ):
            if summ >= target or i == len(nums):
                if summ == target:
                    res.append(path[:])
                return
            #take same number
            dfs(i, path + [nums[i]], summ + nums[i])  
            #not take
            dfs(i+1, path, summ) 

        dfs(0, [], 0)
        return list(map(lambda x: list(x) , set(map(lambda x: tuple(x), res))))
