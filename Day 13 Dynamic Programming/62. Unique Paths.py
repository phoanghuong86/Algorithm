class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        paths = [[0]*(n) for i in range(m)]
        for i in range(m):
            paths[i][0] = 1
        for i in range(n):
            paths[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m-1][n-1]
        
