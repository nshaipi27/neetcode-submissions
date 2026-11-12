class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0 

        rotted = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotted.append((i, j))
        
        
        time_taken = 0

        q = deque(rotted)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            level = len(q)
            rotted_this_level = False
            for _ in range(level):
                i, j = q.popleft()
                for dr, dc in directions:
                    if i + dr < 0 or j + dc < 0 or i + dr >= len(grid) or j + dc >= len(grid[0]):
                        continue
                    if grid[i + dr][j + dc] == 1:
                        grid[i + dr][j + dc] = 2
                        q.append((i + dr, j + dc))
                        rotted_this_level = True
            if rotted_this_level:
                time_taken += 1
            
        for row in grid:
            if 1 in row:
                return -1
        return time_taken 
                    

        