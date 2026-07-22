class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            grid[i][j] = '2'
            for dr, dc in dirs:
                nr, nc = i+dr, j+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    dfs(nr, nc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        
        return res
        