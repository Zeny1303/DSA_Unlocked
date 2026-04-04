class Solution(object):
    
    def dfs(self,i,j, grid,rows,col,dx,dy):
        if i<0 or j<0 or i>=rows or j>=col or grid[i][j]!="1":
            return 
        grid[i][j]="2"
        for k in range(4):
            ii = i+dx[k]
            jj = j+ dy[k]
            self.dfs(ii,jj, grid,rows,col,dx,dy)    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        cnt = 0
        rows = len(grid)
        col = len(grid[0])
        for i in range(rows):
            for j in range(col):
                if grid[i][j] =="1":
                    # land hai 
                    self.dfs(i,j,grid,rows,col,dx,dy)
                    cnt+=1
        return cnt             
        