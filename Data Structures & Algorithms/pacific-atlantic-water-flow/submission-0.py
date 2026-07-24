class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return [[]]

        res = []
        ROWS, COLS = len(heights), len(heights[0])

        self.cache = defaultdict(list) #(r, c) -> [Bool, Bool]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        end_pacific = set((r, 0) for r in range(ROWS)).union((0, c) for c in range(COLS))
        end_atlantic = set((r, COLS-1) for r in range(ROWS)).union((ROWS-1, c) for c in range(COLS))
        
        def dfs(r, c, op, visited):
            if (op == 'p' and (r, c) in end_pacific) or (op == 'a' and (r, c) in end_atlantic):
                return True
            
            visited[r][c] = True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS 
                and 0 <= nc < COLS 
                and not visited[nr][nc] 
                and heights[nr][nc] <= heights[r][c]
                and dfs(nr, nc, op, visited)):
                    return True
            
            return False

        for i in range(ROWS):
            for j in range(COLS):
                should_add = True
                for op in ('a', 'p'):
                    visited = [[False]*COLS for _ in range(ROWS)]  # fresh grid every call
                    if not dfs(i, j, op, visited):
                        should_add = False

                if should_add:
                    res.append([i, j])
        return res
