class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        if len(s) == len(t):
            if Counter(s) == Counter(t):  
                return s
            else:
                return ''
         
        tCounts = Counter(t)
        sCounts = {}
        need = len(tCounts)
        have = 0

        res_len = float("inf")
        res_l, res_r = 0, 0

        l = 0

        for r, ch in enumerate(s):
            if ch in tCounts:
                sCounts[ch] = sCounts.get(ch, 0) + 1
                if sCounts[ch] == tCounts[ch]:
                    have += 1

            # window satisfies all chars
            while have == need:
                # store / update best window
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res_l, res_r = l, r

                # shrink from left
                left_ch = s[l]
                if left_ch in tCounts:
                    sCounts[left_ch] -= 1
                    if sCounts[left_ch] < tCounts[left_ch]:
                        have -= 1
                l += 1

        return "" if res_len == float("inf") else s[res_l:res_r+1]

        