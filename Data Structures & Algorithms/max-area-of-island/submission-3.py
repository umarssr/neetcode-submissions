class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(i,j, area):
            if i <0 or i>=rows or j<0 or j >= cols or grid[i][j] != 1:
                return 0
            else:
                grid[i][j] = 0

                return 1+ dfs(i+1, j, area) +dfs(i-1, j, area)+dfs(i, j+1, area)+dfs(i, j-1, area)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==1:
                    res = max(res,dfs(i,j, 0))
        return res