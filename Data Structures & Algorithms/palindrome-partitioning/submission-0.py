class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1                
            return True

        def helper(i):
            if i >= len(s):
                res.append(part[:])
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    part.append(s[i : j + 1])
                    #explore the other half
                    helper(j + 1)
                    part.pop()
        
        #max of partitions would be (n-1)
        helper(0)
        return res