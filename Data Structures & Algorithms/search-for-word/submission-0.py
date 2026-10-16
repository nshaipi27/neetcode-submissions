class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        path = []
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != word[len(path)]:
                return False
            
            visited.add((i, j))
            path.append(board[i][j])
            if len(path) == len(word):
                return True
            
            for (dr, dc) in directions:
                if dfs(i + dr, j + dc):
                    return True
            path.pop()
            visited.remove((i, j))
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c):
                    return True
        return False