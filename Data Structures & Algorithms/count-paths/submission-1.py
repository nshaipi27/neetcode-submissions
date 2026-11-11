class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1] * n] * m
        for i in range(len(memo) - 2, -1, -1):
            for j in range(len(memo[0]) -2, -1, -1):
                memo[i][j] = memo[i + 1][j] + memo[i][j + 1] 
        return memo[0][0]