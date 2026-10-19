class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        pacific = set()
        atlantic = set()

        def dfs(i, j, ocean, prevHeight):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 
            if (i, j) in ocean:
                return 
            
            if heights[i][j] < prevHeight:
                return 
            
            ocean.add((i, j))
            
            for dr, dc in directions:
                dfs(i + dr, j + dc, ocean, heights[i][j])
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols-1])
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows-1][c])
        
        return list(atlantic & pacific)






