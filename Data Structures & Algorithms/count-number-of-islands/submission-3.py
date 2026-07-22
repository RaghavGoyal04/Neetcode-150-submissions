class DSU:
    def __init__(self):
        self.parents = {}

    def find(self, u):
        ur, uc = u[0], u[1]
        if self.parents[(ur, uc)] != (ur, uc):
            self.parents[(ur, uc)] = self.find(self.parents[(ur, uc)])
        return self.parents[(ur, uc)]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        # I'm checking if these islands - u & v are already same
        if pu == pv:
            return False
        
        #if not same we merge into 1 island and thus reduce the overall count
        if pu < pv:
            self.parents[pv] = pu
        else:
            self.parents[pu] = pv
        
        return True


class Solution:
    # for this we will use disjoint union concept
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        
        dsu = DSU()
        
        # fill in all islands i.e '1' 
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dsu.parents[(i, j)] = (i, j)
                    islands += 1
        
        #then we try to merge them
        # if we can then we reduce the island counts 
        # if not - they were then already a part of the island and not seperate
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    for dr, dc in dirs:
                        nr, nc = i + dr, j + dc 
                        if (
                            0 <= nr < ROWS and
                            0 <= nc < COLS and
                            grid[nr][nc] == '1' and 
                            dsu.union((i, j), (nr, nc))
                        ):
                            islands -= 1
        return islands



        