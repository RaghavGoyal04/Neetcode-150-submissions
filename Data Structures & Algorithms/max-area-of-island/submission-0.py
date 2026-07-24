class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            nonlocal res, count
            grid[r][c] = 2
            res = max(res, count)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                    # print((nr, nc), grid[nr][nc])
                    count += 1
                    dfs(nr, nc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # print('main entry point: ', (r, c), grid[r][c])
                    count = 1
                    dfs(r, c)
        return res

