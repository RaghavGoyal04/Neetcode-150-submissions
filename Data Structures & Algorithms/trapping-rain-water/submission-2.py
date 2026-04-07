class Solution:
    def trap(self, height: List[int]) -> int:
        # left_b = [heights[0]]*len(heights)
        # right_b = [heights[-1]]*len(heights)

        # for i in range(1, len(heights)):
        #     left_b[i] = max(left_b[i-1], heights[i])
        
        # for i in range(len(heights)-2, -1, -1):
        #     right_b[i] = max(right_b[i+1], heights[i])
        
        # # print(left_b, right_b)

        # max_w = 0
        # for i in range(len(heights)-1):
        #     cur_w = min(left_b[i], right_b[i]) - heights[i]
        #     max_w += cur_w
        
        # return max_w
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        res = 0

        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if l_max <= r_max:
                res += (l_max - height[l])
                l += 1
            else:
                res += (r_max - height[r])
                r -= 1
        return res

