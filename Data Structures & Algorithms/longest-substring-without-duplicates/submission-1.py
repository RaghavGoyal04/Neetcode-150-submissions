class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not n: return 0
        # l, r = 0, 0
        # res = 0
        # seen = set()
        # while r < n:
        #     while l < r and s[r] in seen:
        #         seen.remove(s[l])
        #         l += 1
        #     res = max(res, r-l+1)
        #     seen.add(s[r])
        #     r += 1
        # return res

        l, r = 0, 0
        seen = dict()
        res = 0
        while r < n:
            if s[r] in seen:
                l = max(seen[s[r]]+1, l)
            seen[s[r]] = r
            res = max(res, r-l+1)
            r += 1
        return res