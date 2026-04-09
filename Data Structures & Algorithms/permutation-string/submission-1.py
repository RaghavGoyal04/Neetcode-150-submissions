class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        l = 0
        k = len(s1)
        n = len(s2)
        s1_counter = Counter(s1)
        for r in range(k, n+1):
            if Counter(s2[l:r]) == s1_counter:
                return True
            l += 1
        return  False

        