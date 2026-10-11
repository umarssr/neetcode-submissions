class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                area = 0
                if grid[i][j] == 1:
                    stack = [(i,j)]
                    grid[i][j] = 0
                    while stack:
                        i,j = stack.pop()
                        area+=1
                        if i+1 < rows and grid[i+1][j] == 1:
                            grid[i+1][j] =0
                            stack.append((i+1,j))
                        if i-1 >=0 and grid[i-1][j] ==1:
                            grid[i-1][j] = 0
                            stack.append((i-1, j))
                        if j+1 < cols and grid[i][j+1] == 1:
                            grid[i][j+1] =0
                            stack.append((i,j+1))
                        if j-1 >=0 and grid[i][j-1]==1:
                            grid[i][j-1] = 0
                            stack.append((i, j-1))
                    max_area = max(max_area, area)
        return max_area



                    