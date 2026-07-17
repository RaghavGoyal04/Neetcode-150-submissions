class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(board), len(board[0])
        visited = [[False]*cols for _ in range(rows)]

        def helper(r, c, path):
            #exit if they match
            if path == word:
                return True

            #early exit if the len becomes bigger
            if len(path) > len(word):
                return False

            #mark the visited array
            visited[r][c] = True
            
            #look for neighbouring elements
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    if helper(nr, nc, path + board[nr][nc]):
                        return True

            #unmark the visited array
            visited[r][c] = False
            return False

        #1. check every start (row, col) pair and 
        #then call backtracking func
        for i in range(rows):
            for j in range(cols):
                if helper(i, j, board[i][j]): 
                    return True
        return False
