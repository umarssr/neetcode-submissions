class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(i,j, area):
            if i <0 or i>=rows or j<0 or j >= cols or grid[i][j] != 1:
                return area
            else:
                grid[i][j] = 0
                area+=1
                area= dfs(i+1, j, area)
                area= dfs(i-1, j, area)
                area= dfs(i, j+1, area)
                area= dfs(i, j-1, area)
                return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==1:
                    res = max(res,dfs(i,j, 0))
        return res