class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_a, max_h = 0, 0
        while l < r:
            max_h = min(heights[l], heights[r])
            max_a = max(max_a, max_h * (r-l))
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return max_a
