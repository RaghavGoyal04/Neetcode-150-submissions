class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: return 
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([])
        #fill the q with treasure points
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: 
                    q.append((r,c, 0))
        
        #traverse the q in BFS fashion
        while q:
            r, c, step = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] not in (-1, 0) and grid[nr][nc] > step+1):
                    grid[nr][nc] = step + 1
                    q.append((nr, nc, step+1))
        
