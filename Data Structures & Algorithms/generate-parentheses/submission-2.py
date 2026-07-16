class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n: return []
        res= []
        def backtrack(o, c, path):
            if o == n and c == n:
                res.append(''.join(path))
                return
            
            if o < n:
                path.append('(')
                backtrack(o+1, c, path)
                path.pop()
            
            if c < o <= n:
                path.append(')')
                backtrack(o, c+1, path)
                path.pop()

        backtrack(0, 0, [])
        return res
        