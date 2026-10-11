class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    res+=1
                    self.dfs(grid, i, j, rows, cols, grid)
        return res
    def dfs(self,graph, i, j, rows, cols, grid):
        if i <0 or i >=rows or j <0 or j >= cols or grid[i][j]!='1':
            return
        else:
            grid[i][j] = '0'
            self.dfs(graph,i, j+1, rows, cols, grid)
            self.dfs(graph,i, j-1, rows, cols, grid)
            self.dfs(graph,i+1, j, rows, cols, grid)
            self.dfs(graph,i-1, j, rows, cols, grid)




                




        

