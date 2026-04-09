class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        l, r = 0, 0
        maxFreq = 0
        freqs = defaultdict(int)
        while r < n:
            freqs[s[r]] += 1
            maxFreq = max(maxFreq, freqs[s[r]])

            # window size = r - l + 1
            # we can keep window while chars_to_change <= k

            while (r - l + 1) - maxFreq > k :
                freqs[s[l]] -= 1
                l += 1 
            
            res = max(res, r-l+1)
            r += 1
        return res
