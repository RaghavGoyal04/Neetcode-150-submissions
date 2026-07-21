class DSU:

    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    
    def union(self, node1, node2):
        pu, pv = self.find(node1), self.find(node2)
        if pu == pv:
            return False
        
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True
            

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        #very interesting!!!
        def index(r, c):
            return r * COLS + c
        
        # 1. Count all land cells initially
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != '1':
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS 
                        and 0 <= nc < COLS 
                        and grid[nr][nc] == '1'
                        and dsu.union(index(r, c), index(nr, nc))
                    ):
                        islands -= 1
        return islands
