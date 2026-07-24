class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([])
        #fill the q with treasure points
        total_fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: 
                    total_fresh += 1
                elif grid[r][c] == 2: 
                    q.append((r,c))
        
        # print(q, total_fresh)

        #traverse the q in BFS fashion
        total_time = 0
        visited_fresh = 0
        while q:
            rotted_this_round = False
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        visited_fresh += 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        rotted_this_round = True
            if rotted_this_round:
                total_time += 1
        
        # print(q, total_time, visited_fresh, total_fresh)

        return total_time if visited_fresh == total_fresh else -1

        