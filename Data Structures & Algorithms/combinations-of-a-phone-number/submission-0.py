class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        c_map = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        res = []
        if not digits: 
            return res
        
        for c in digits:
            if c not in c_map:
                return res

        def helper(i, path):
            if i >= len(digits):
                res.append(''.join(path[:]))
                return

            for letter in c_map[digits[i]]:
                path.append(letter)
                helper(i+1, path)
                path.pop()

        helper(0, [])

        return res