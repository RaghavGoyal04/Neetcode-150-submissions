class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []

        c_map = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        cache = {}
        
        def helper(i):
            if i == len(digits):
                return ['']

            if i in cache:
                return cache[i]

            res = []
            # Get the letters for the current digit
            for letter in c_map[digits[i]]:
                # Combine the current letter with all suffixes from the next index
                for suffix in helper(i + 1):
                    res.append(letter + suffix)

            cache[i] = res
            return res

        return helper(0)