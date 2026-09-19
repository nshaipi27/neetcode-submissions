class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += (matrix.pop(0))

            if matrix and matrix[0]: # we pop the last element of every row
                for row in matrix:
                    res.append(row.pop())
            
            if matrix: #go backwards on last row
                res += (matrix.pop()[::-1])

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res