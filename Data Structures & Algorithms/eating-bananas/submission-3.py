class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursSoFar(m):
            hours_so_far = 0
            for pile in piles:
                hours_so_far += math.ceil(pile/m) 
                # print(f'{m=}, {math.ceil(pile/m)=}, {hours_so_far=}')
            return hours_so_far

        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l)//2
            sofar = hoursSoFar(m)
            # print(sofar, l, r, m)
            if sofar <= h:
                r = m
            else:
                l = m+1
        return r

# piles = [1,4,3,2], h = 9
# l, r, m -> 1, 10, 5 is_valid: [1/5,4/5,3/5,2/5] = 4 
# l, r, m -> 1, 5, 3 is_valid: [1/3,4/3,3/3,2/3] = 1+2+1+1 = 5 
# l, r, m -> 1, 3, 2 is_valid: [1/2,4/2,3/2,2/2] = 1+2+2+1 = 6
# l, r, m -> 1, 2, 1 is_valid: [1/1,4/1,3/1,2/1] = 1+4+3+2 = 10
# l, r, m -> 2, 2, 2 : break return r
