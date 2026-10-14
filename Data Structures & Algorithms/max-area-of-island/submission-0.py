class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        curr_area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            nonlocal curr_area
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 
            if grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            curr_area += 1

            for (dr, dc) in directions:
                dfs(i + dr, j + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, curr_area)
                    curr_area = 0
        return max_area