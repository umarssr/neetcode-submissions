from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = deque()
        time = 0

        # find the rotten fruit.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh +=1
        while queue and fresh > 0:
            for _ in range(len(queue)):

                r,c = queue.popleft()
                if r+1 < rows and grid[r+1][c] == 1:
                    queue.append((r+1, c))
                    fresh-=1
                    grid[r+1][c] = 2
                if r-1 >= 0  and grid[r-1][c] ==1:
                    queue.append((r-1, c))
                    fresh-=1
                    grid[r-1][c] = 2
                if c+1 < cols and grid[r][c+1] ==1:
                    queue.append((r, c+1))
                    fresh-=1
                    grid[r][c+1] = 2
                if c-1 >= 0 and grid[r][c-1] == 1:
                    queue.append((r, c-1))
                    fresh-=1
                    grid[r][c-1] = 2
            time +=1
        
        if fresh == 0:
            return time 
        else:
            return -1

