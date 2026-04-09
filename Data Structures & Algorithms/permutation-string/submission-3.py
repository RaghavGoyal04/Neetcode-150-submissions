class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        l = 0
        k = len(s1)
        n = len(s2)
        s1_counter = Counter(s1)
        

        # for i in range(k, n+1):
        #     if Counter(s2[l:i]) == s1_counter:
        #         return True
        #     l += 1
        # return  False

        window = Counter(s2[:k])
        if window == s1_counter: return True

        for i in range(k, n):
            window[s2[i]] += 1      # add new char
            window[s2[i - k]] -= 1  # remove old char
            if window[s2[i - k]] == 0:
                del window[s2[i - k]]          # keep it clean
            
            if window == s1_counter:
                return True
        
        return False



        
        
        