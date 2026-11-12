class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        safe = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if board[i][j] == 'X':
                return
            if (i, j) in safe:
                return
            safe.add((i, j))

            for dr, dc in directions:
                dfs(i + dr, j + dc)
                
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols -1] == 'O':
                dfs(r, cols - 1)
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in safe:
                    board[r][c] = 'X'

