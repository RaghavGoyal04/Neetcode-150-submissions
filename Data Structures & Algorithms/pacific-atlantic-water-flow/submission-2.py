class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        end_pacific = set((r, 0) for r in range(ROWS)).union((0, c) for c in range(COLS))
        end_atlantic = set((r, COLS-1) for r in range(ROWS)).union((ROWS-1, c) for c in range(COLS))
        common_p = set()
        common_a = set()

        def dfs(r, c, reachable):
            if (r, c) in reachable:
                return
            
            reachable.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS 
                and 0 <= nc < COLS 
                and heights[nr][nc] not in reachable
                and heights[r][c] <= heights[nr][nc]):
                    dfs(nr, nc, reachable)

        for i, j in end_pacific:
            dfs(i, j, common_p)
        
        for i, j in end_atlantic:
            dfs(i, j, common_a)
        
        return list(common_p.intersection(common_a))