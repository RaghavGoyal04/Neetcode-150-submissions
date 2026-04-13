class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows*cols-1
        while l <= r:
            m = l + (r-l)//2
            r_m = m // cols
            c_m = m % cols
            if matrix[r_m][c_m] == target:
                return True
            elif matrix[r_m][c_m] > target:
                r = m-1
            else:
                l = m+1
        return False
        