class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []

        c_map = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        res = []

        def helper(i, path):
            if i == len(digits):
                res.append(path)
                return

            # Get the letters for the current digit
            for letter in c_map[digits[i]]:
                helper(i+1, path + letter)

        helper(0, '')
        return res