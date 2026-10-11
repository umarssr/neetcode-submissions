from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid), len(grid[0])
        q=deque()
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))
        distance = 0
        def add_to_queue(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j] == -1 or (i,j) in visited:
                return
            else:
                q.append((i,j))
                visited.add((i,j))
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                add_to_queue(r+1, c)
                add_to_queue(r-1, c)
                add_to_queue(r, c+1)
                add_to_queue(r, c-1)
            distance+=1


        
        



