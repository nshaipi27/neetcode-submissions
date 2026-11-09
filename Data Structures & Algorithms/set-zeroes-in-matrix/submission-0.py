class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for r in rows:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0