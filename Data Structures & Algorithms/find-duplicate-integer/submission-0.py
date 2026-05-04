class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [-1]*(n+1)
        for i in range(n):
            if seen[nums[i]] == 1:
                return nums[i]
            seen[nums[i]] = 1

