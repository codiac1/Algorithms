class Solution:
    def bfs_dfs(self, x, y , mat):
        if self.dp[x][y] != -1:
            return self.dp[x][y]
        self.dp[x][y] = 1
        
        for d in self.directions:
            nx = x + d[0]
            ny = y + d[1]
            
            if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and mat[nx][ny] > mat[x][y]:
                if self.dp[nx][ny] == -1:
                    self.bfs_dfs(nx,ny, mat)
            
                self.dp[x][y] = max(self.dp[x][y] , 1+self.dp[nx][ny])
                            
                
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        ans = 0
        
        if rows == 1 and cols == 1:
            return 1
        
        self.dp = [[-1 for _ in range(cols)] for _ in range(rows)]
        self.directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        for i in range(rows):
            for j in range(cols):
                self.bfs_dfs(i, j , mat)
                ans = max(ans , self.dp[i][j])
        return ans
        
        