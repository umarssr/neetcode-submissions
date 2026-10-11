from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        starts = []
        minutes = 0
        fresh = 0
        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    starts.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1
        queue = deque(starts)
        
        while queue and fresh >0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr>=0 and nr <rows and nc >=0 and nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -=1
            minutes +=1
        return minutes if fresh == 0 else -1
        

            
