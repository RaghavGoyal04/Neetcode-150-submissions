class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(r, c, grid):
            #vertical
            for i in range(r):
                if grid[i][c] == 'Q':
                    return False

            #left diagonal
            d = 1
            while r - d >= 0 and c - d >= 0 :
                if grid[r - d][c - d] == 'Q':
                    return False 
                d +=1 

            #right diagonal
            d = 1
            while r - d >= 0 and c + d < n :
                if grid[r - d][c + d] == 'Q':
                    return False 

                d += 1  
  
            return True

        res = []

        def dfs(r, grid):
            #breaking condition
            if r == n:
                res.append([''.join(row) for row in grid])
                return

            for c in range(n):
                if is_safe(r, c, grid):
                    grid[r][c] = 'Q'
                    dfs(r+1, grid)
                    grid[r][c] = '.'

        grid = [ ['.' for _ in range(n)] for _ in range(n)]
        dfs(0, grid)
        return res
        