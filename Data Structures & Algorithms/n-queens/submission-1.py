class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        rows, cols = n, n
        res = []

        def is_safe(r, c):
            #safe vertical
            for i in range(r):
                if board[i][c] == 'Q':
                    return False

            #safe left d
            i, j = r, c
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i-1, j-1

            #safe right d
            a, b = r, c
            while a >= 0 and b < cols:
                if board[a][b] == 'Q':
                    return False
                a, b = a-1, b+1
            return True

        def helper(r, board):
            if r == rows:
                board_flatten = [''.join(r) for r in board]
                res.append(board_flatten[:])
                return 
            for c in range(cols):
                if is_safe(r, c):
                    board[r][c] = 'Q'
                    helper(r+1, board)
                    board[r][c] = '.'
        
        helper(0, board)
        return res