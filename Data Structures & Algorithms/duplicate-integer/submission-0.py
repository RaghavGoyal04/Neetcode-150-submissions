class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return any(v > 1 for v in Counter(nums).values())

        