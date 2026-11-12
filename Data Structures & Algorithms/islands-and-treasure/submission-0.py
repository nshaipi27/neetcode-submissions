class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if grid is None:
            return 

        treasure = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasure.append((i, j))
        
        if len(treasure) == 0:
            return 
        
        q = deque(treasure)
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q:
            i, j = q.popleft()

            for dr, dc in directions:
                if i + dr < 0 or j + dc < 0 or i + dr >= len(grid) or j + dc >= len(grid[0]):
                    continue
                if grid[i + dr][j + dc] == 2**31 - 1 :
                    grid[i+dr][j+dc] = grid[i][j] + 1
                    q.append((i + dr, j + dc))
                
            
