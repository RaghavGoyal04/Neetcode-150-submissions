class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPali(part_str):
            l, r = 0, len(part_str)-1
            while l < r:
                if part_str[l] != part_str[r]:
                    return False
                l, r = l+1, r-1
            return True
        
        def helper(start, part):
            # Base Case: If we've processed the entire string, 
            # the current partition path is valid!
            if start >= len(s):
                res.append(part.copy())
                return
            
            # The loop checks all possible substrings starting at 'start'
            for i in range(start, len(s)):
                #check if starting string is palind then move forward
                part_str = s[start : i + 1]
                if isPali(part_str):
                    helper(i+1, part + [part_str])

        helper(0, [])
        return res

        